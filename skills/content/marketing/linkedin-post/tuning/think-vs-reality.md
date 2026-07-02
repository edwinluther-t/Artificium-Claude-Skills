## Tuning think-vs-reality

One template, THREE layouts toggled by `<body data-layout="...">`. Only the
matching block renders. Pick the layout, then fill that block.

**1. Layout choice:**
- `minimal` — the contrast is a single line each (belief vs fact). House
  dark-tech theme, `1080×1350`. Use when there's no list to show.
- `rich-divider` — each side has multiple points (icon-grid and/or a ✓/✗ list),
  and you want a clean editorial split with NO panels — a center divider line
  separates them. Light green(belief)/red(reality) theme, `1080×1250`.
- `rich-image` — same rich content, but each side LEADS with a hero image
  (e.g. calm person vs overwhelmed person) for emotional contrast. Same theme/size.

**2. Asymmetry is the point.** Belief-vs-reality is not two equal peers (that's
`versus-list`). The left (belief) side is deliberately lighter — a short lead
line + a few breezy ✓ items. The right (reality) side carries the weight — an
icon-grid of real concerns + a ✓ list of what the work actually is. Don't force
them equal; the imbalance IS the message. (If both sides are genuinely equal and
valid, you want `versus-list`, not this.)

**3. Canvas height per layout** — set `--h` in `:root` AND `--window-size`:
minimal → `1080,1350`; rich modes → `1080,1250` (default). If the right side
gets very long (8 grid chips + 5 list items), bump rich to `1080,1350`. Too much
empty bottom on the left is expected given the asymmetry; only grow the canvas
when the RIGHT side overflows.

**4. Hero images can't be generated here.** In `rich-image` each `.hero` is a
slot showing a placeholder freehand icon by default. To use real art, replace
the `.ph` span with `<img src="...">` (supplied file/data-URI). For the two
contrasting characters, hand the user a prompt-recipe:

> "Flat illustration, [calm person leaning back at laptop / stressed person head
> in hands at laptop], [green / red] accent, soft shading, white background,
> landscape, no text." — one per side, matching the green/red sides.

Never claim to have rendered the characters.

**5. Rendering a specific mode (gotcha).** To script a render in a non-default
mode, replace ONLY the real `<body data-layout="rich-image">` TAG — NOT every
`data-layout="..."` occurrence. The head comment AND the CSS selectors
(`body[data-layout="..."] .X{...}`) contain that substring; a greedy/`count=1`
regex hits the head COMMENT first and leaves the real tag unchanged (tell:
identical render bytes). Match the exact literal `<body data-layout="rich-image">`.
(Related: a same-specificity `.wrap{display:flex}` rule once overrode the
`.L{display:none}` toggle and stacked all layouts — keep `display` OFF the shared
`.wrap` class; let the active-layout selector own it.)

**6. Icons.** Rich modes use `streamline-freehand` (verify names resolve first —
see the freehand gotcha under "Tuning whiteboard-sketch"). ✓ =
`form-validation-check-square-1`, ✗ = `form-validation-remove-square`. Tint each
side's icons with its `--think` (green) / `--real` (red) var (already wired).

---
