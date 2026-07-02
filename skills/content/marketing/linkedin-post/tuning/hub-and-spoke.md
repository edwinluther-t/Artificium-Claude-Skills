## Tuning hub-and-spoke

One template, two layouts toggled by `<body data-layout="...">`. Only the
matching block renders. Pick the layout, then fill that block.

**1. Layout choice:**
- `split` (default) — left TITLE block + right radial RING of up to 6 nodes
  around a glyph+label hub + a bottom 3-cell stat strip. Light-indigo theme,
  landscape `1200×760`. Use for a "resource hub / everything for X" post where
  the title and a headline metric strip share the frame with the ring.
- `centered` — eyebrow + title stacked ABOVE a centered hub, spokes placed
  around it (4 wired; s5/s6 exist). House dark-tech theme, portrait `1080×1350`.
  Use for a simpler "one core, a few parts" diagram with no stat strip.

**2. Node count (split).** Six seats are wired (`.n1`–`.n6`) at even clock
positions: top, right-top, right-bottom, bottom, left-bottom, left-top. For
fewer nodes, delete the extra `.node`s — the dashed ring stays. 3 nodes → use
n1/n3/n5 (triangle); 4 → n1/n2/n4/n5 or the four cardinal seats. Don't exceed 6
at this canvas (cards collide); for 7+ small items use `cheatsheet-grid`.

**3. Connector simplification (honest note).** The source draws an individual
dashed spoke from the hub to each card. This template uses ONE dashed ring behind
the cards instead — it reads the same (radial connection) and is far more robust
than six angled line segments needing per-node trig. If you truly need per-spoke
lines, add positioned `.conn` pseudo-elements per node; not worth it by default.

**4. Stat strip (split).** The bottom `.stats` is a fixed 3-cell grid
(badge-icon + big number + label). Edit the numbers/labels; for 2 or 4 stats
change `grid-template-columns:repeat(N,1fr)` and add/remove `.stat` cells.
Delete the whole `.stats` block if the post has no headline metrics — the ring
still fills the frame.

**5. Content.** Node `<h3>` is 1–2 short words (it's a label, not a sentence).
The hub `.lab` is one short word/phrase. Title supports a 2-line `h1` with a
`.hl` accent span on the second line. Keep it STRUCTURE-ONLY: neutral
placeholders, never the source's product/brand names.

**6. Toggle discipline (gotcha).** `display` is kept OFF the shared `.L` wrapper;
only `body[data-layout="x"] .L-x{display:flex}` turns a layout on — a shared
`display` rule of equal specificity would stack both layouts. When scripting a
non-default render, replace the EXACT `<body data-layout="centered">` tag, not
the same substring in the head comment / CSS selectors (a `count=1` regex hits
the comment first; tell = identical render bytes).

---
