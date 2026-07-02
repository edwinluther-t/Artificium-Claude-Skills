## Tuning cover-hero

An article/blog/link cover: a bold headline over a full-bleed hero. The HEADLINE
is the identity; the background sets mood. Landscape `1200×630` by default. This
archetype intentionally does NOT match a source layout — it ships a self-contained
sci-fi CSS scene so it works with zero supplied art. All adaptation is markup edits
+ three `data-*` knobs — never a second template.

**1. Background (`data-bg` on `<body>`).**
- `css` (default) — the built-in sci-fi scene: a layered radial-glow gradient, a
  `.grid` perspective horizon, and a `.net` glowing connector-node network (a `.hub`
  + four `.s` satellite nodes joined by an SVG gradient-line group). Fully renders
  here, no art needed. Recolor via the `--cyan/--violet/--magenta` and `--bg1..3`
  vars. Move/relabel nodes by editing the `.nN` position rules + their Lucide icons.
- `image` — drop a real hero photo by setting `background-image` on `.imgbg`; the
  CSS grid + network auto-hide and the scrim keeps the headline legible. Use a dark
  or busy-but-dimmable image; the scrim covers the lower ~74%.

**2. Connector network (`data-net` on `<body>`).** `on` (default) shows the
node network; `off` hides it for a cleaner gradient-only cover. The SVG line
endpoints are hand-placed to approximate node anchors — if you reposition nodes,
nudge the `<path>` coordinates to match (they don't auto-track; close enough reads
as an abstract network, don't pixel-chase).

**3. Kicker (`data-kicker` on `<body>`).** `on` (default) shows the top mono
kicker chip (category/tag). `off` removes it. Edit its Lucide glyph + text.

**4. Headline.** `.head` is the big Space Grotesk headline; wrap the phrase you
want emphasized in `<span class="hl">` for the cyan→violet→magenta gradient. Keep
it to 2–3 lines; it sits in the lower third over the scrim. The `.meta` row is a
"who" mark (left) + a mono tag/handle (right) — this is the footer for THIS
archetype (it has no separate `.foot`); replace with the end-user's brand/handle
per Layout Rule #3.

**5. Size.** Landscape `1200×630` (LinkedIn link-preview / cover ratio). For a
square feed cover set `--w/--h` to `1080×1080` and `--window-size` to match; the
scene + scrim reflow. For portrait, `1080×1350`. Change `--w/--h`, the SVG
`viewBox`, AND `--window-size` together.

**6. Honest scope.** The source reference for this archetype was an AI-generated
illustration (robots, depth, 3D glow) that CANNOT be produced here. This template
does not reproduce it — it offers a renderable CSS sci-fi scene instead, or an
image slot for the user's own art. Don't claim the CSS scene is the source art;
it's an original stand-in. STRUCTURE/COPY is neutral: headline, kicker, and meta
are placeholders — never paste a source's title or branding.

---
