## Tuning carousel-slide

This is a SLIDE SYSTEM, not a single graphic. One template renders one slide;
you build a deck by rendering it once per page with different data + mode.

**1. Slide modes** — set on `<body data-slide="...">`, only the matching block
shows:
- `cover` — title + `· N pages` + hero slot + two-box thesis stack + next-cue.
  Use for slide 1.
- `list` — section title + glass callout + up to 3 icon/heading/subtext rows +
  next-cue. Use for "here are the points" slides.
- `statement` — uppercase kicker + one large centered statement (with green
  emphasis `<b>`) + next-cue. Use for punchy single-idea slides.

To add modes (e.g. a 2-column or CTA slide), add a `.s-xxx` block + a
`body[data-slide="xxx"] .s-xxx{display:flex}` rule — DON'T make a second template.

**2. Build a deck (the actual workflow).** For an N-slide carousel:
- Decide the slide order and which mode each slide uses (typical 6-page:
  cover → statement(hook) → list(reality) → list/statement(concept) →
  list(how) → statement(CTA)).
- For EACH slide: set `data-slide`, edit that block's text, set the `.count`
  (`Page NN / TT`) and the `.kicker` to match, set the `.nextcue` to the NEXT
  slide's title (drop `.nextcue` on the final slide).
- Render each to `slideNN.png`. The render harness must replace ONLY the
  `<body data-slide="cover">` tag, not occurrences in CSS selectors — editing
  the CSS `body[data-slide=...]` rules breaks the toggle and stacks every slide
  (a real bug hit during build; the tell is a huge PNG with overlapping content).
- Deliver the numbered PNGs as the carousel; LinkedIn accepts them as a document
  / multi-image post.

**3. Per-slide fields that are NOT auto-derived — set them by hand each render:**
- `.count` page number (e.g. `Page 03 / 06`).
- `.kicker` ("03 · Concept").
- `.nextcue` label.
These are plain data in the markup; forgetting them leaves the previous slide's
values (e.g. counter stuck on `01`).

**4. Content density per mode:** `list` holds 3 rows comfortably at `1080×1350`;
a 4th is fine if subtext is short. `statement` wants ≤ 14 words. `cover` thesis
≤ 2 lines. Short slides intentionally leave lower whitespace — that's on-brand
for a deck; do not pad.

**5. Visuals / honest limit:** the source's glossy 3D icons + robot mascot are
NOT reproducible here (image-gen unavailable). This template uses CSS
glass/glow + flat Lucide icons. For the 3D look, swap a `.hero .iconify` or
`.lrow .ic` for `<img src="...">` with supplied art, or hand the user a
prompt-recipe:

> "Glossy 3D render, [subject], dark background, teal-green and gold neon
> rim-light, glass material, centered, square." — adjust subject per slide.

Never claim to have rendered 3D art.

---
