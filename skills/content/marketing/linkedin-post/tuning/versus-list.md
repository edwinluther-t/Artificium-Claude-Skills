## Tuning versus-list

One template, two center modes, variation via markup. Decide before rendering:

**1. Center mode** — set on the `<body data-center="...">`:
- `divider` (default) — vertical rule + round "VS" badge. Renders fully here.
  Use this unless the user supplies art.
- `image` — shows the `.center .slot`. Replace the `.ph` placeholder div with
  `<img src="...">` pointing at a supplied illustration/photo (file path or data
  URI). The columns auto-narrow to make room.

**2. The image cannot be generated here.** This environment is HTML/CSS → PNG
only; there is no image-generation model available. Do NOT claim to render the
mascot/illustration. When `image` mode is wanted, either (a) ask the user to
supply the asset, or (b) hand them a prompt-recipe to run in their own image
tool, then drop the result into the slot. Prompt-recipe shape:

> "Flat vector illustration, [subject] at a laptop, soft rounded style, pastel
> purple/blue palette (#4f46e5 / #9333ea), white background, friendly, centered,
> portrait 3:4, no text." — adjust subject/colors to match the post.

**3. Content balance** — both columns should have the **same row count** (the
reference used 6/6). Each row is one short clause + one icon. 4–7 rows per side
fits portrait `1080×1350`; 8+ → drop font to 20px or split the post. Keep the
two column captions parallel in length so the header pills line up.

**4. Match the source palette.** This template defaults to its soft-light theme.
If a future "A vs B" post comes from a different reference, re-sample that
reference's hex into the palette block rather than reusing this
one — per the reference-matching rule above.

---
