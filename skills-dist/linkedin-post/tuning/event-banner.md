## Tuning event-banner

An event promo. The LEFT column (logo → title → tagline → meta → CTA) is the
identity; the RIGHT icon-badge cluster is the decorative feature zone. Landscape
`1200×627` by default. All adaptation is markup edits + three `data-*` knobs —
never a second template.

**1. Icon-badge cluster (`data-badges` + `data-chips` on `<body>`).** The right
side is a 3-column grid: filled dark-circle icon badges (`.badge.fill`, Lucide) +
outlined white info chips (`.badge.chip`, short text like "LIVE & LOCAL", "LEVEL
100–300", "LABS"). Defaults: `data-badges="6"` (6 filled) + `data-chips="3"`
(3 chips) = the source's 3×3. Knobs: `data-badges` 4/5/6 trims filled badges from
the end; `data-chips` 0/2/3 trims chips. Pick semantically-true Lucide icons for
the badges and validate names (`/lucide.json?icons=...`) first. Chips carry 1–2
short uppercase lines (a `<small>` makes the second line) — they're feature/level
tags, not sentences.

**2. The swoosh (`data-swoosh` on `<body>`).** `on` (default) draws the curved
right panel (`clip-path:path(...)`) behind the cluster — matches the source. `off`
removes it (cluster sits on the flat bg) for a simpler banner. To reshape the
curve, edit the `.swoosh` `clip-path` path coordinates; it's a single cubic-Bézier
S-curve sized to the 1200×627 canvas — re-tune the control points if you change
`--w/--h`.

**3. Left column anatomy.** `.logo` (a `.mark` Lucide glyph + a `.name`) →
`.title` (big 2-line Space Grotesk; the second line takes `.l2` for the white
half of a two-tone title) → `.tag` (one-line tagline) → `.meta` (Space Grotesk;
first line is format · sessions, a `.sub` span is the lighter date line) → `.cta`
(dark pill + arrow). Keep the title to 2 short lines; it's the largest element.

**4. Two-tone title.** The source splits the title across two colors (dark word /
white word). `.title .l2` is the white line; drop the class for a single-color
title. For a 1-line title, remove the `<br>` and `.l2`.

**5. Size.** Landscape `1200×627` (LinkedIn link-preview / event-banner ratio).
For a feed-portrait variant set `--w/--h` to `1080×1350`, stack the cluster BELOW
the left block (change `.wrap` to one column), and reduce to `data-badges="4"`
`data-chips="2"`. Change `--w/--h`, the `.swoosh` path, AND `--window-size`
together.

**6. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted event-promo
banner. SHIP THE LAYOUT, NOT THE WORDS: the event name, tagline, dates, session
count, brand/logo, and chip labels stay neutral placeholders ("EVENT / NAME",
"Format | N Sessions", "LABS"). Never paste the source's event name, brand, logo,
or copy into the template or a generated post.

---
