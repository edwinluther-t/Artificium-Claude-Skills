## Tuning person-spotlight

A person announcement. The LEFT column (headline → sub → bio rows) + the RIGHT
hero (portrait + name plate) are the identity; the two bottom bands are optional.
Square `1080×1080` by default. All adaptation is markup edits + four `data-*`
knobs — never a second template.

**1. Hero portrait (`data-hero` on `<body>`).** The source's right side is a
cut-out PHOTO over a building backdrop with a glowing 3D circuit overlay — the
photo and the 3D art CANNOT be generated here. So:
- `image` (default) — `.hero .photo` is a background-image slot. Fill it by setting
  `background-image` on `.photo` (a supplied portrait PNG, ideally a cut-out on a
  dark/transparent bg so the chip ring + plate read over it). Over the photo, a CSS
  `.ring` (a glowing chip `.core` + four Lucide `.orb` icons) approximates the
  source's circuit decoration, and a `.plate` shows the name/role. Honest split:
  the PORTRAIT is user-supplied; the ring + plate are CSS — never claim to have
  rendered the photo or the 3D overlay.
- `css` — no photo; `.photo` shows a "PORTRAIT SLOT" label. Use only for layout
  preview. For delivery, supply a portrait.

Prompt-recipe for the portrait (hand to the user's image tool):

> "Professional cut-out portrait of [person], arms crossed, confident, studio
> lighting, on a transparent / dark-navy background, upper-body, facing camera,
> high resolution, no text." — then composite or drop into the slot.

**2. Bio rows (`data-bio` on `<body>`).** Default `"4"` (matches the source's four
points); `"3"` hides the 4th. Each `.brow` = a round outline Lucide badge + a 2–4
line `.bt` with accent keywords via `<b>`. Keep each to ≤ 3 lines. Pick
semantically-true Lucide icons (credential→`cpu`/`award`, team→`users`,
scope→`contact`, reporting→`id-card`) and validate names first.

**3. Quote band (`data-quote` on `<body>`).** `on` (default) shows the value-prop
band: big quote mark + a one-line statement (accent `<b>` keywords) + a brand
logo lockup on the right. `off` removes it. Edit the `.logo` glyph + text to the
poster's brand (placeholder by default).

**4. Engagement band (`data-engage` on `<body>`).** `on` (default) shows a follow
prompt + a Like/Comment/Share/Follow row (Lucide). `off` removes it. This mirrors
the source's social-CTA strip; drop it for a cleaner poster.

**5. Headline + sub.** `.head` is the huge 2-line gradient headline (Space
Grotesk, blue→violet clip). `.sub` is the "Name joins ORG as ROLE" line with the
role in accent `<b>`. Keep the headline to ≤ 2 short lines — it's the largest
element and the gradient needs room.

**6. Size.** Square `1080×1080` (matches the source). Dropping BOTH bands
(`data-quote="off" data-engage="off"`) frees vertical space — consider `1080×1080`
still, or `1080×1350` portrait if you add more bio rows. Change `--w/--h` AND
`--window-size` together.

**7. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted appointment
post. SHIP THE LAYOUT, NOT THE WORDS: the person name, role, org, bio facts,
quote, brand/logo, and handle stay neutral placeholders ("Person Name", "Role
Title", "Organization"). Never paste the source's real person, employer, prior
employer, quote, or logo into the template or a generated post.

---
