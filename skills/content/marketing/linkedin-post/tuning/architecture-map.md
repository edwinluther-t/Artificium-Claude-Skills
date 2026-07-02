## Tuning architecture-map

A connected system diagram. The center MAP is the identity; rails and banner are
optional. Everything is built from a few repeatable connector pieces — don't add
a second template for a different topology, recombine these.

**1. The center is a STACK OF TIERS (the dominant element, ~55-60% width), not a
thin vertical chain.** Compose it from:
- `.maphead` — the colored section header bar (e.g. "Solution Architecture").
- `.tier data-n="2|3|4"` — one row of `.node`s (peer boxes). `data-n` sets the
  column count.
- `.tconn` — the vertical down-arrow between tiers.
- `.band data-n="3|4"` — a WIDE tier: a labelled box (`.blab`) holding a sub-row
  of `.bcell` items (e.g. a Data Layer with several stores).
- `.wpanels` → two `.wpanel`s — the final tier of two wide list panels (e.g.
  integration zones). Variants `.red .green`.
- `.node` accent variants `.v .g .t .r .a`.
A typical map: maphead → tier(3) → tier(3) → band(4) → tier(4) → wpanels.

**2. Rails** — set `data-rails` on `.layout`: `"2"` (default, LEFT + right rails
— matches the source three-zone look), `"1"` (RIGHT rail only, wider map), `"0"`
(map only, full width). Layout
uses `grid-template-areas` per value (`"M R"` / `"L M R"` / `"M"`) so a hidden
rail leaves no gap. The two rails are DIFFERENT structures on purpose:
- **Right rail** (`.rail` of `.rpanel`s) = SEPARATE boxed panels, each a titled
  icon-list (Principles / Tools / Delivers). Accent variants `.v .g .t`.
- **Left rail** (`.lrail` → ONE `.lpanel` of `.lcat` sections) = a single tall
  panel of stacked category sections (icon → heading → sub-bullets), like a
  skills/expertise column. Per-category accents `.b .v .g .t .a .r`.
GOTCHA (cost several re-renders): the left rail element is class `lrail` ONLY —
NOT `rail lrail`. If it also carries `rail`, the later `.rail{grid-area:R;
display:flex}` rules hijack it into the RIGHT column (overlapping the right rail)
and override its scoped hide. Keep the two rails on separate class names —
same-specificity, source-order CSS collisions are the recurring bug here.

**3. Size / orientation.** LANDSCAPE `1350×1080` is the default (architecture
reads wide; matches the source). For a feed-portrait version, set `--w/--h` to
`1080×1350` and drop to `data-rails="0"` or `"1"` with a shorter map (3–4 trunk
nodes) — two rails + full map will NOT fit portrait. Change `--w/--h` AND
`--window-size` together.

**4. Density is the trap.** The source crammed a full map + two rails + a tool
logo list + banner; at 1080–1350px that's an unreadable wall. Keep the trunk to
~3–4 nodes + one branch row; keep each rail to ≤ 3 panels of ≤ 4 items; node
labels are 1–2 words + a one-line `.meta`. If you need more, split into two posts.

**5. Icons + theme.** Clean flat Lucide (medium is flat-tech; do NOT use
`streamline-freehand` here). Per-section accent vars already wire icon colors.
Validate any new Lucide name (`/lucide.json?icons=...`) before use.

**6. CONTENT IS STRUCTURE-ONLY.** This archetype is distilled from real,
copyrighted LinkedIn architecture posts. SHIP THE LAYOUT, NOT THE WORDS: every
node label, rail item, and banner line stays a neutral placeholder ("Entry",
"Core", "Node A", "Tool one"). Never paste the source's product names, stack
names, logos, headings, or taglines into the template or a generated post.

---
