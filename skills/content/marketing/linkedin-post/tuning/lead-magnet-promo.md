## Tuning lead-magnet-promo

A download-driver. The LEFT column (title → benefit rows → CTA) is the identity;
the RIGHT cover card is the lead-magnet render. Portrait `1080×1350` by default.
All adaptation is markup edits + two `data-*` knobs — never a second template.

**1. Benefit rows (`data-items` on `.body` … set on `<body>`).** Default `"4"`
matches the source (4 benefit rows; a 5th `.row` is wired but hidden). `"3"` hides
rows 4–5; `"5"` shows all five and tightens the gap. Each row = a round badge icon
(`.bi`, Lucide) + a 2-line `.rt` label. Keep labels to ≤ 4 words/line. Pick
semantically-true Lucide icons and validate names (`/lucide.json?icons=...`) first.

**2. Cover panel (`data-cover` on `<body>`).** The source's right panel is a glossy
3D tablet showing a cover with a PHOTOGRAPHIC hero — neither the 3D device nor the
photo can be generated here. So:
- `card` (default) — a flat tilted cover card on a CSS pedestal: logo slot +
  one-line descriptor → image slot (`.cover .img`, defaults ON) → tag (e.g.
  "FACTSHEET") → title → subtitle → URL. Fill the image slot by setting
  `background-image` on `.cover .img`; retheme by swapping `--cover-*` vars. This
  is an honest CSS approximation, NOT a real device mockup.
- `image` — the whole cover becomes ONE background-image slot (the inner
  logo/tag/body hide). Drop a finished device-mockup PNG via `background-image` on
  `.cover`. Use this when you have real rendered art.

For the cover hero or a real 3D device render, hand the user a prompt-recipe:

> "Glossy 3D tablet/device mockup, floating at a slight angle, showing a [asset
> title] cover with a [subject] hero image, soft purple studio background, premium
> product-shot lighting, no text besides the cover." — adjust to the asset.

Never claim to have rendered the 3D device or the photo.

**3. CTA pill.** `.cta` is a dark glowing pill (mint ring + glow): a round star
badge + a 2-line label ("Download / The Asset"). Edit the label; it's the single
action. Keep it 1–2 short words per line. Don't add a second CTA — one action.

**4. Title.** `.h-muted` is the lighter 2-line lead (e.g. "N Core / Section"),
`.h-bold` the heavy 2-line payload below it. Both are Poppins. Keep each to 2
lines; the left column is narrow (half the canvas).

**5. Size.** Portrait `1080×1350` (matches the source). For a square variant when
the benefit list is only 2–3 items, set `--w/--h` to `1080×1080` and use
`data-items="3"`; change `--w/--h` AND `--window-size` together.

**6. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted lead-magnet
post. SHIP THE LAYOUT, NOT THE WORDS: the title, benefit labels, brand/logo, asset
title, subtitle, and URL stay neutral placeholders. Never paste the source's
product name, brand, logo, asset title, or copy into the template or a generated
post.

---
