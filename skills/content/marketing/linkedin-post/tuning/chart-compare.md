## Tuning chart-compare

A two-up chart comparison. The TWO CHARTS are the identity — the contrast between
a sparse pie and a dense radial fan IS the message. Square `1080×1080` by default.
The charts are real CSS (no images); all adaptation is markup/var edits + two
`data-*` knobs — never a second template.

**1. Left chart — sparse PIE (`data-slices-l` on `<body>`).** A conic-gradient
disc. `data-slices-l` 3/4/5 swaps to a pre-built conic-gradient with that many
slices (default 4). To change the slice SIZES, edit the `conic-gradient` stops in
the matching rule (each `--pN COLOR start% end%`). The `.plabels span` (pl1..pl4)
are absolutely positioned slice labels — move/relabel them to sit on their slice;
they don't auto-place. Keep the pie to ≤ 5 slices — that's the "concentrated" side.

**2. Right chart — dense radial BAR-FAN.** Built by the inline `<script>`: `N`
bars (default 14) spoke out from the hub, each rotated `360/N · i` with a length
from the `lens[]` array (varying heights = diversified texture). To retune: change
`N`, edit `lens[]` (one length per bar, px past the hub), or change the `cols[]`
var cycle. Geometry that MUST hold (this was the build bug): each `.bar` is
`bottom:0` on the zero-size `.wheel` center point with `transform-origin:50% 100%`
and `transform:rotate(a)` — the bottom edge pins at center and the bar fans
outward. Do NOT use `translateY`/`transform-origin:50% 0` (that knots all bars
above the hub — the first render's failure). The hub disc (`z-index:3`) covers the
inner `hub`-radius stub of every bar.

**3. Asymmetry is the point.** Left = FEW big slices (concentrated/bad); right =
MANY small spokes (diversified/good). Don't equalize them — the visual density gap
carries the argument. The wheel reads "busier", not necessarily bigger; that's
correct.

**4. Captions + verdicts.** Each panel has a `.cap` (red caption) + a `.verdict`
(Lucide trend icon + one short line). `.verdict.bad` tints the icon red,
`.verdict.good` green (already wired). Keep verdicts to ≤ 4 words.

**5. CTA (`data-cta` on `<body>`).** `on` (default) shows the red pill CTA; `off`
removes it. Edit the label + keep the arrow.

**6. Size + theme.** Square `1080×1080` (matches the source). Defaults to the
silver-grey/red palette per the reference-matching rule. For a dark theme, swap
`--bg/--ink/--muted` and keep the chart hues. Change `--w/--h` AND `--window-size`
together if resizing.

**7. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted comparison
post. SHIP THE LAYOUT, NOT THE WORDS: the headline, slice/segment labels,
captions, verdicts, brand, and CTA stay neutral placeholders. Never paste the
source's brand, product names, or copy into the template or a generated post.

---
