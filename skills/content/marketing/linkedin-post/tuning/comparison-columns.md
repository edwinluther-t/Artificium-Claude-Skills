## Tuning comparison-columns

This is the one template whose look depends on content. The template is fixed —
all adaptation is done by editing three things in the markup, never by adding
new templates. Decide each before rendering:

**1. Column count.** Set `data-cards` on the `.cols` element to match the number
of `.card` blocks, and delete/add cards to match:
- 3 components → `<div class="cols" data-cards="3">` + three `.card` blocks
  (use classes `c1 c2 c3`).
- 4 components → `data-cards="4"` + four cards (`c1 c2 c3 c4`).
- Never use 2 (use `before-after` / `think-vs-reality`) or 5+ (too cramped at
  LinkedIn width — split into two posts or use `cheatsheet-grid`).

**2. Canvas size — pick by list length (cards stretch to equal height, so the
shortest column dictates how much empty space shows):**

| Items per column | Canvas (`--w` × `--h`, `--window-size`) | Why |
|---|---|---|
| 2–3 short items | `1080 × 1080` (square) | tall portrait leaves dead space; square fills |
| 4–5 items | `1080 × 1350` (portrait, default) | the reference density; fills cleanly |
| 6+ items / long text | `1080 × 1350`, shrink card font to 15px | keep it from overflowing |

To change canvas: edit `--w/--h` in the palette block **and** match
`--window-size=W,H` in the render command. Change both or it crops.

**3. Content density — keep columns balanced.** Equal-height cards mean one long
column stretches all the others. Rules:
- Aim for the **same item count** in every column (±1). If one component has
  fewer real points, merge or cut elsewhere — don't leave one column half-empty.
- Keep each list item to **one short clause** (≤ 4–5 words ideal). Two-line wraps
  are fine; three-line items break the rhythm.
- The `Output` box is one short phrase. The bottom `banner` is one sentence with
  one bolded payoff. Drop the banner entirely (delete the `.banner` div) if the
  point is already obvious — don't pad.
- Title supports up to 4 multi-color words via `.a .b .c .d` spans + `.plus`
  separators. For non-"X + Y" titles, use a single `.title` span and a normal
  `h1`-style line instead.

If after these the card interiors still look hollow, the content is too thin for
this archetype — switch to `hub-and-spoke` (fewer points, one center) instead.

---
