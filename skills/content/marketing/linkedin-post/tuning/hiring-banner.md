## Tuning hiring-banner

A recruitment / announcement banner. The HERO band (badge → role title → tagline
+ art) is the identity; the 3-zone info band is the supporting detail. Landscape
`1200×750` by default. All adaptation is markup edits + two `data-*` knobs —
never a second template.

**1. Hero art slot (`data-hero` on `.hero`).** The source's hero is a glossy 3D
illustration (cloud + product icons) that CANNOT be generated here (no image-gen
model). So `.art` DEFAULTS to an image slot, not clip-art:
- `image` (default) — drop real art by setting `background-image` on `.art`
  (a supplied PNG/SVG file path or data-URI). Do NOT replace it with flat Lucide
  icons pretending to be the 3D art — that breaks the source match. Use the
  prompt-recipe to make the art, then fill the slot:

  > "Glossy 3D render, [subject — e.g. a cloud with stacked database / table /
  > factory icons], deep navy background, electric-blue rim light, glass material,
  > floating, centered, landscape, no text." — adjust subject to the role.

- `off` — collapse the art zone; the hero title goes full-width (a clean
  text-only banner). Use when no art is available and you don't want a placeholder.

Never claim to have rendered the 3D art.

**2. Info zones (`data-zones` on `.info`).** Default `"3"` matches the source
(primary skills + secondary expertise + callout/CTA). `"2"` = two skill columns,
no callout (move the CTA into the hero tagline). `"1"` = one skill column +
callout. The CTA chip lives inside `.callout`, so dropping the callout drops the
CTA — keep a CTA somewhere (hero or callout).

**3. Content density.** Primary column holds 6 skills comfortably; secondary 4.
Keep each to one short clause. The callout `.punch` is ≤ 3 short lines with one
bolded payoff each; the CTA `.ct` is a label + one line. If a column runs long,
shrink `.col li` font to 15px rather than growing the canvas — landscape height
is fixed for feed.

**4. Size.** Landscape `1200×750` (matches the source's banner ratio). For a
feed-portrait variant set `--w/--h` to `1080×1350`, stack the hero ABOVE the info
band (the grid already wraps), and reduce to `data-zones="2"`. Change `--w/--h`
AND `--window-size` together.

**5. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted hiring post.
SHIP THE LAYOUT, NOT THE WORDS: the role title, skill names, taglines, and CTA
stay neutral placeholders ("Open Role Title Here", "Skill one"). Never paste the
source's role name, stack/tool names, company logo, or copy into the template or
a generated post.

---
