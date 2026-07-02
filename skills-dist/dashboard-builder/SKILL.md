---
name: dashboard-builder
description: Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard instead of a vanity board.
---

# Dashboard Builder

Use this when the task is to build a dashboard people can operate from.

The goal is not "show every metric." The goal is to answer:

- is it healthy?
- where is the bottleneck?
- what changed?
- what action should someone take?

## When to Use

- "Build a Kafka monitoring dashboard"
- "Create a Grafana dashboard for Elasticsearch"
- "Make a SigNoz dashboard for this service"
- "Turn this metrics list into a real operational dashboard"

## Guardrails

- do not start from visual layout; start from operator questions
- do not include every available metric just because it exists
- do not mix health, throughput, and resource panels without structure
- do not ship panels without titles, units, and sane thresholds

## Workflow

### 1. Define the operating questions

Organize around:

- health / availability
- latency / performance
- throughput / volume
- saturation / resources
- service-specific risk

### 2. Study the target platform schema

Inspect existing dashboards first:

- JSON structure
- query language
- variables
- threshold styling
- section layout

### 3. Build the minimum useful board

Recommended structure:

1. overview
2. performance
3. resources
4. service-specific section

### 4. Cut vanity panels

Every panel should answer a real question. If it does not, remove it.

## Example Panel Sets

### Elasticsearch

- cluster health
- shard allocation
- search latency
- indexing rate
- JVM heap / GC

### Kafka

- broker count
- under-replicated partitions
- messages in / out
- consumer lag
- disk and network pressure

### API gateway / ingress

- request rate
- p50 / p95 / p99 latency
- error rate
- upstream health
- active connections

## Layout & Color (readability of the board itself)

A dashboard is regions, not a pile of panels. Apply the same layout/color
discipline used for any UI surface:

- **Region grouping = the top-to-bottom reading order operators actually use:**
  a header row (title + the key SLO/status at a glance), then rows grouped by
  concern (traffic → latency → errors → saturation), most-important row first.
  Treat each row like a section band; don't scatter related panels.
- **One coherent palette, semantic color only.** Reserve hue for meaning:
  green/amber/red for status and thresholds, a single neutral accent for normal
  series. Don't color series decoratively — it reads as noise. Keep text/line
  contrast ≥ 4.5:1 on the board's background; on dark themes lighten muted labels.
- **Consistent color mapping across panels:** the same service/series is the same
  color everywhere on the board, so the eye tracks it between panels.
- **Chart type by question, not by variety:** time-series for trends, stat/gauge
  for a single current number vs threshold, bar for ranked comparison, heatmap for
  distribution. Pick the sparsest viz that answers the operator's question.
- **Density:** left-align labels, right-align numbers, put units on every panel,
  and cut any panel that doesn't change a decision (the "no vanity panels" rule).

## Quality Checklist

- [ ] valid dashboard JSON
- [ ] clear section grouping
- [ ] titles and units are present
- [ ] thresholds/status colors are meaningful
- [ ] same series = same color across all panels
- [ ] one coherent palette; hue reserved for status/meaning, not decoration
- [ ] label/number contrast is legible on the board theme (≥ 4.5:1)
- [ ] variables exist for common filters
- [ ] default time range and refresh are sensible
- [ ] no vanity panels with no operator value

## Related Skills

- `observability-and-instrumentation`
- `backend-patterns`
- `terminal-ops`
