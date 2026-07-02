## Tuning animated-flow-map

The ONE animated archetype. A tall portrait stack of numbered LAYER bands joined
by connectors that carry moving flow dots. Live HTML animates; export is a still
PNG or a looping GIF.

**1. Anatomy.** `title` (+ `.hl` accent word) → `.subpill` (one positioning
line) → `.body` grid of three columns: left `.tiers` (numbered `.tier-lab` rail,
one per layer), center `.stack` (the `.layer` bands), right `.takeaways` (the
numbered summary rail) → `.foot` (social handles). The center stack is the star.

**2. A layer band = `.layer lN` → `.lhead` + `.row data-n="3|4|5"` of `.box`es.**
Between consecutive layers put a `.conn cN` (`.track` dashed line + `.dot` flow
dot + `.arrow`). The `lN`/`cN` classes (1–5) pick the per-layer accent. Add or
remove whole `.layer`+`.conn` pairs to fit the system; 3–5 layers is the sweet
spot at this canvas. Keep boxes to ≤5 per row (`data-n`), label = 1–2 words +
optional one-line `.m`.

**3. THE ANIMATION (the point of this archetype).** Each `.conn .dot` runs
`@keyframes flow{from{left:18%}to{left:82%}}` on a 2.4s linear infinite loop —
dots travel source→destination continuously. This runs in any browser; the
committed template ships the motion. NO `data-phase` attribute = live animation.

**4. Exporting.** This machine renders HTML→PNG/GIF only (no ffmpeg, no MP4):
- **Still PNG** — render as-is (dots get frozen wherever the capture lands). Use
  the standard pipeline at `1080×1500`.
- **Looping GIF** — capture several phase-stepped frames and stitch with PIL.
  The template exposes `<body data-phase="0".."5">` which PAUSES the animation and
  places every dot at fraction k/5 along its path; 6 frames = one full loop. The
  bundled helper `make_flow_gif.py` (ships next to the templates) automates it:
  `python make_flow_gif.py <out.gif>` — it swaps `<body>`→`<body data-phase="k">`
  for k=0..5, screenshots each with headless Chrome (1× scale to bound size),
  then `PIL.Image.save(save_all=True, append_images=..., duration=140, loop=0,
  disposal=2)`. Use `optimize=False` or PIL collapses near-duplicate frames (a
  6-frame loop came out as 3 with optimize on). Output ~470 KB at 1080×1500×6.
  To add frames, raise `STEPS` and add matching `body[data-phase="k"]` rules.
- **GIF gotcha:** `data-phase` is set by replacing the bare `<body>` tag (the only
  `<body>` with no attribute). Don't hand-add an attr to the committed template or
  the live animation stops — keep the shipped template's `<body>` bare.

**5. Right takeaways rail.** Fixed 8-item numbered list (`.take` → `.tnum` +
`h5` + `p`), accent cycling via `:nth-child`. For fewer takeaways delete `.take`
rows; the rail uses `justify-content:space-between` so it stays evenly spread.
Drop the whole `.takeaways` column (and widen the grid) if the post has no
summary list.

**6. Density / honest limits.** This is the densest archetype — 5 layers × 4–5
boxes + an 8-item rail is near the readable ceiling at portrait width. Don't add a
6th layer without shrinking box font. The source's hand-drawn arrows between
specific boxes are simplified to one straight inter-layer connector per gap
(per-box arrows would need a lot of fragile absolute positioning) — the flow dot
carries the "data moves down the stack" meaning. STRUCTURE-ONLY: neutral
placeholders, never the source's layer names, copy, takeaways, or social handles.

---
