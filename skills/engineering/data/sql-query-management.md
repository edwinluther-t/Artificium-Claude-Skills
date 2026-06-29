---
name: sql-query-management
description: Use when writing, reviewing, or optimizing SQL queries — including DDL, DML, migrations, and stored procedures. Use when designing table structures, managing schemas, or diagnosing query performance issues.
---

# SQL Query Management

Standards for writing, organizing, and maintaining SQL across a project.

## The Non-Negotiable Rules

**Never create objects in the public schema.** Every table, view, function, sequence, and index belongs in a named schema. `public` is a trap: it's the default, it bypasses schema-level permissions, and it makes access control ambiguous.

```sql
-- Wrong
CREATE TABLE users (...);

-- Right
CREATE TABLE app.users (...);
```

**Always qualify object names with the schema.** Even inside a function that operates on a single schema. Ambiguity is not free.

```sql
-- Wrong
SELECT * FROM users WHERE id = $1;

-- Right
SELECT * FROM app.users WHERE id = $1;
```

## Schema Design

### Naming

- Schema names: lowercase, short, domain-meaningful (`app`, `auth`, `billing`, `analytics`, `audit`)
- Table names: lowercase, plural, snake_case (`app.user_accounts`, `billing.invoices`)
- Column names: lowercase, snake_case (`created_at`, `is_active`, `external_ref_id`)
- Primary keys: `id` (not `user_id` — the table name already provides that context)
- Foreign keys: `{referenced_table_singular}_id` (`user_id`, `invoice_id`)

### Every table needs

```sql
CREATE TABLE app.orders (
    id          bigserial PRIMARY KEY,
    -- domain columns
    created_at  timestamptz NOT NULL DEFAULT now(),
    updated_at  timestamptz NOT NULL DEFAULT now()
);
```

`created_at` and `updated_at` are mandatory. Use `timestamptz`, never `timestamp` — timezone-naive timestamps create bugs in multi-region systems.

### Soft deletes

Use a `deleted_at timestamptz` column, not a boolean `is_deleted`. A timestamp tells you when; a boolean doesn't. Always filter soft-deleted rows explicitly.

```sql
SELECT * FROM app.orders WHERE deleted_at IS NULL;
```

## Query Patterns

### SELECT

Never use `SELECT *` in application code. Name every column. Implicit column ordering breaks when the schema changes.

```sql
-- Wrong
SELECT * FROM app.users WHERE id = $1;

-- Right
SELECT id, email, display_name, created_at FROM app.users WHERE id = $1;
```

### Parameterize everything

No string concatenation for query values. Use parameterized queries or prepared statements. Always.

```sql
-- Wrong (SQL injection vector)
query = "SELECT * FROM app.users WHERE email = '" + email + "'"

-- Right
SELECT id, email FROM app.users WHERE email = $1
-- with: [email]
```

### Joins

Always use explicit JOIN syntax. Never implicit joins via WHERE.

```sql
-- Wrong
SELECT u.email, o.total
FROM app.users u, app.orders o
WHERE u.id = o.user_id;

-- Right
SELECT u.email, o.total
FROM app.users u
JOIN app.orders o ON o.user_id = u.id;
```

### Aggregations

Never aggregate without knowing whether NULLs matter. `COUNT(*)` counts rows; `COUNT(column)` counts non-null values — use the right one explicitly.

## Migrations

- One concern per migration file. Don't combine schema changes with data backfills.
- Migrations must be idempotent where possible (`CREATE TABLE IF NOT EXISTS`, `CREATE INDEX CONCURRENTLY IF NOT EXISTS`).
- Never drop a column or table in the same migration that removes the application code that references it. Deploy the code change first; drop the column in a subsequent migration after the deploy is stable.
- Always provide a rollback. If the migration tool doesn't enforce it, write it as a comment.

```sql
-- Migration: 0042_add_billing_schema.sql
-- Rollback: DROP SCHEMA billing CASCADE;

CREATE SCHEMA IF NOT EXISTS billing;

CREATE TABLE billing.invoices (
    id          bigserial PRIMARY KEY,
    user_id     bigint NOT NULL REFERENCES app.users(id),
    amount_cents integer NOT NULL,
    status      text NOT NULL DEFAULT 'pending',
    created_at  timestamptz NOT NULL DEFAULT now(),
    updated_at  timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX idx_billing_invoices_user_id ON billing.invoices(user_id);
CREATE INDEX idx_billing_invoices_status  ON billing.invoices(status) WHERE deleted_at IS NULL;
```

## Indexes

- Index foreign keys by default.
- Use partial indexes for filtered queries that are common (`WHERE status = 'active'`, `WHERE deleted_at IS NULL`).
- Use `CREATE INDEX CONCURRENTLY` in production to avoid table locks.
- Name indexes explicitly: `idx_{table}_{column(s)}`.

## Performance

Before optimizing, read the plan:

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT ...;
```

Look for: Sequential Scans on large tables, Nested Loop joins on large sets, high actual vs. estimated row counts (stale statistics → run `ANALYZE`).

Fix in this order:
1. Missing index
2. Query rewrite (avoid functions on indexed columns in WHERE)
3. Schema change (denormalize only as a last resort)

## Stored Procedures and Functions

- Always specify the schema: `CREATE FUNCTION app.calculate_tax(...)`.
- Use `SECURITY DEFINER` only when necessary and document why.
- Prefer `RETURNS TABLE` over `RETURNS SETOF record` for clarity.
- Keep business logic out of the database where possible — the database is for data integrity, not application logic.

## Access Control

Grant at the schema level, not the table level, unless you need column-level security.

```sql
-- Application role: read/write to app schema only
GRANT USAGE ON SCHEMA app TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA app TO app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA app TO app_user;

-- Analytics role: read-only across reporting schemas
GRANT USAGE ON SCHEMA analytics TO analytics_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO analytics_reader;
```

Never grant `public` schema permissions to application roles.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Objects in `public` schema | Name and use a schema for every object |
| `SELECT *` in application queries | Name columns explicitly |
| `timestamp` instead of `timestamptz` | Always use `timestamptz` |
| Implicit joins | Use explicit `JOIN ... ON` syntax |
| Dropping columns same deploy as code removal | Code change first, column drop after stability confirmed |
| Unparameterized queries | Parameterize everything, no exceptions |
| Indexes without explicit names | Name with `idx_{table}_{columns}` pattern |
