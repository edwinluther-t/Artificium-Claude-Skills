## Tuning layered-loop-map

The SECOND animated archetype. Several stacked left→right pipelines whose connectors
carry moving direction dots, led by an optional VS comparison and closed by a maturity
row. Portrait-tall `1080×1400` by default. Live HTML animates; export is a still PNG or
a looping GIF. All adaptation is markup edits + four `data-*` knobs (plus `data-phase`
for capture) — never a second template.

**1. Anatomy.** `.title` (two-tone: `.a` indigo / `.b` violet) + `.subt` (italic
subhead) → `.vs` (optional VS header) → `.stack` (the layer bands) → `.scale`
(maturity chevron row) → `.cta` band + `.foot`.

**2. VS comparison header (`data-vs` on `<body>`).** `on` (default) shows two
`.vpanel`s (`.l` / `.r`) each a `.vhead` label + a `.vgrid` of `.vstep`s (Lucide icon +
short label) — two small "loop diagram" panels — separated by a round `.vsbadge` (VS).
`off` removes the whole header (the stack starts at the top). The steps are a compact
icon grid (a stand-in for the source's arrowed loop; the loop arrows are simplified to
a grid — the point is the two contrasting step-sets, not the arrows). Keep `.vl` labels
to ≤ 2 short words. This is what distinguishes this archetype from a plain flow map —
keep it on when the post contrasts two approaches.

**3. Layer bands (`data-layers` on `<body>`).** Default `"4"` (matches the source's
four layers); `"3"` hides the 4th band. Each `.layer.lN` = a `.lhead` (colored italic
band title) + a `.pipe` (the left→right chain). The `lN` class (1–4) picks the band
accent (`--L1..--L4`). To add a 5th layer, add `--L5`, a `.layer.l5` block, and a
`body[data-layers="5"]` show rule — but 4 is the readable ceiling at this height.

**4. The pipeline + ANIMATED dots (the point).** Inside `.pipe`, alternate `.pnode`
boxes (Lucide `.pi` + `.h4` + optional `.pm`) with `.lk` connectors. Each `.lk` =
`.track` (dashed line) + `.dot` (the moving dot) + `.arrow`. The `.dot` runs
`@keyframes flow{from{left:8%}to{left:82%}}` on a 1.8s loop, colored by the band
accent. This animates live in any browser — the committed template ships the motion.
Keep 4 nodes + 3 connectors per band (more crowds the row); node labels 1–2 words.

**5. Maturity-scale row (`data-scale` on `<body>`).** `on` (default) shows the
`.scaleh` title + `.chevs` (4 dashed `.chev` cells: Lucide icon + `<h5>` + `<p>`),
accent-cycling. `off` removes it. This is the source's bottom "maturity scale" — a
progression of roles/levels. For 3 or 5 cells change `grid-template-columns` and
add/remove `.chev`s.

**6. CTA (`data-cta` on `<body>`).** `on` (default) shows the full-width purple CTA
band (bleeds to canvas edge). `off` removes it. One action — edit the label.

**7. Exporting (same pipeline as animated-flow-map).** HTML→PNG/GIF only (no ffmpeg):
- **Still PNG** — render as-is at `1080×1400` (dots freeze wherever capture lands).
- **Looping GIF** — the bundled `make_flow_gif.py` is SHARED by both animated
  archetypes; pass the template name:
  `python make_flow_gif.py <out.gif> layered-loop-map`
  It swaps the real `<body ...>` tag to `<body ... data-phase="k">` for k=0..5
  (freezing every dot at fraction k/5 along its path), screenshots each frame, and
  stitches with PIL (`save_all`, `loop=0`, `disposal=2`, `optimize=False`). ~70 KB.
- **GIF/phase gotcha:** the `data-phase` swap targets the REAL `<body ...>` tag via a
  regex (`<body\b[^>]*>`) — this template's `<body>` HAS attributes (`data-vs` etc.),
  unlike animated-flow-map's bare `<body>`; the helper handles both (it strips any
  existing `data-phase` then injects the new one). The head comment and the CSS
  `body[data-phase="k"]` selectors are NOT matched (no leading `<`). Keep the shipped
  template's `<body>` free of `data-phase` so the live animation runs.

**8. Size.** Portrait-tall `1080×1400`. Dropping the VS header (`data-vs="off"`) or a
layer frees height — the `.stack` uses `justify-content:space-between` so bands stay
evenly spread. Change `--w/--h` AND `--window-size` together (and the `SIZES` entry in
`make_flow_gif.py` if you want the GIF default to match).

**9. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted layered explainer
poster. SHIP THE LAYOUT, NOT THE WORDS: the title, VS steps, layer/node labels, maturity
levels, CTA, and handle stay neutral placeholders ("Concept A", "Layer 1 — Stage One",
"Node A", "Level One"). Never paste the source's names, copy, or social handles into the
template or a generated post.

---
