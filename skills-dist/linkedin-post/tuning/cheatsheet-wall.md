## Tuning cheatsheet-wall

A dense whole-topic reference poster. The MASONRY of mixed panels IS the identity;
the two-tone title and footer CTA frame it. Portrait-tall `1080×1580` by default
(the wall needs the height). All adaptation is markup edits (add/drop/reorder
`.panel` blocks) + one `data-*` knob — never a second template.

**1. The wall is a CSS-`column` masonry.** `.wall{column-count:2}` flows the
`.panel` blocks into two balanced columns; each panel is `break-inside:avoid` so it
never splits. To make a panel FULL WIDTH (spanning both columns) add `.span2`
(`column-span:all`) — used for the commands list. Order in the source flows
top-to-bottom per column; reorder `.panel`s in the HTML to rebalance. Add or remove
whole `.panel` blocks freely — the masonry reflows.

**2. Panel types (each is a drop-in block under a blue `.ph` header).** Mix and
match:
- **code** — a `<pre>` block (`.c` = dim comment, `.k` = accent keyword) + optional
  `<p>`/`<ul>` around it.
- **flow diagram** — `.flows` (3 `.flowcol`s), each a `.ft` title + a `.chain` of
  `.nd` nodes separated by `.ar` arrows; `.pair` puts two nodes side by side (a
  parallel/branch step). Plus `.flownote` bullets below.
- **file-tree** — a `.tree` `<div>` (monospace, `white-space:pre`); wrap directory
  names in `<span class="d">` (accent) and comments in `.c`. Hand-draw the
  ├─ └─ │ box characters.
- **funnel / layered stack** — `.funnel` of `.fband.l1/.l2/.l3` bands; widths step
  down (100/82/64%) to read as a funnel. This REPLACES the source's 3D funnel (see
  honest-limits below). Retint via `--f1/--f2/--f3`.
- **compare columns** — `.cmp` grid (col / `.vs` glyph / col / `.vs` / col), each
  `.cmpcol` an `<h4>` + a short `<ul>`. The `.vs` is a red Lucide glyph.
- **list** — a plain `<ul>` (blue bullets); add `style="column-count:2"` for a
  two-up command list in a `.span2` panel.

**3. CTA band (`data-cta` on `<body>`).** `on` (default) shows the full-width
purple footer band (bleeds to the canvas edge via negative margin); wrap the
highlight word in `<span class="hl">` for the yellow. `off` removes it. Edit the
hook line — keep it one line.

**4. Title.** `.title` is the big two-tone Archivo headline: `.a` (red) + `.b`
(ink). Keep it to ~2–3 words per color so it fits two lines centered. The `.logo`
lockup below it is a small brand mark — replace per Layout Rule #3.

**5. Density + size.** This is the densest archetype. ~7 panels at `1080×1580` is
near the readable ceiling; if a column runs long the wall clips at the bottom (the
CTA/footer get cut — the build bug, fixed by bumping height to `1580` and keeping
panels tight). If you add panels, raise `--h` AND `--window-size` together, or drop a
panel. Keep panel body font ≥ 13px; code ≥ 13px. For a shorter post use fewer panel
types — it still reads as a wall with 4–5.

**6. Honest scope.** The source's glossy 3D funnel and the small COMMANDS-panel
illustration CANNOT be generated here. The funnel is an honest CSS layered-stack
approximation (stacked tinted bands), and illustrations are dropped or swapped for a
flat Lucide icon — never claim to have rendered the 3D art.

**7. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted reference
poster. SHIP THE LAYOUT, NOT THE WORDS: the title, panel headers, code, tree paths,
node labels, commands, brand/logo, and CTA stay neutral placeholders ("Topic Name",
"cmd one", "Step 1"). Never paste the source's product name, brand, logo, code, or
copy into the template or a generated post.

---
