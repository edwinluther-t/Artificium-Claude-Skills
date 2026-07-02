## Tuning partnership-banner

A partnership / merger announcement. The two-logo "A × B" LOCKUP + the gradient
HEADLINE + the COMBINED-SCALE stat row are the identity; the proof strip and
capability strip are supporting. Near-square `1080×1150` by default. All adaptation is
markup edits + four `data-*` knobs — never a second template.

**1. Two-logo lockup (the defining feature).** `.lockup` = `.logo.a` + a `.cross` (×)
+ `.logo.b`. Each `.logo` is a `.lmark` (icon glyph in a rounded chip) + a `.lname`
(wordmark). Defaults are Lucide placeholders. For real brands, either (a) swap the
Lucide glyph and the `.lname` text, or (b) replace `.lmark`'s content with a real logo
image (`background-image` on `.lmark`, or an `<img>`). The `.a` mark is orange, the
`.b` mark mint — retint per brand. Keep wordmarks short; two long names wrap the
lockup. NEVER paste a real company's logo/name into the committed template — those are
supplied at apply-time.

**2. Hero band (`data-hero` on `<body>`).** The source's hero is a photoreal
earth-from-space glow — CANNOT be generated here. So:
- `image` (default) — `.hero .img` is a `background-image` slot. It renders as a plain
  dark band until you supply art (an honest empty state). Fill it via `background-image`
  on `.hero .img`. Prompt-recipe for the art:

  > "Cinematic earth horizon from space at night, glowing blue-and-orange atmospheric
  > rim light, dark starfield, wide panoramic band, subtle light-arc streaks, no text."

- `css` — a self-contained CSS horizon-glow band (a dark arc + a blue→white→orange
  rim-light gradient + a bright seam line). Renders complete with zero art. Use this
  when you have no image. Recolor via the gradient stops in `.hero .css`. Never claim
  the CSS glow is the source's real earth photo — it's an original stand-in.

**3. Stat row (`data-stats` on `<body>`).** Default `"5"` matches the source (5
icon+number+label cells with hairline dividers). `"4"` hides the 5th cell and rebalances
to 4 columns. Each `.stat` = a Lucide `.si` icon + a big `.sn` number + a caps `.sl`
label (1–2 short lines). Keep numbers punchy (`$2.9B`, `46K+`); the label is the metric
name. Pick semantically-true Lucide icons and validate names (`/lucide.json?icons=...`).

**4. Proof strip (`data-proof` on `<body>`).** `on` (default) shows the rounded
3-cell "N of TOP M" panel (each `.pf` = a colored Lucide icon + a `.pn` headline like
"7 of Top 10" + a `.pd` segment label). `off` removes it. The three accents are
`.b1` mint / `.b2` orange / `.b3` cyan. Keep the `.pd` to ≤ 2 short lines.

**5. Capability strip (`data-caps` on `<body>`).** `on` (default) shows the 6-icon
bottom strip (Lucide glyph + a short caps label — AI/Cloud/Data/ERP/CX/Eng). `off`
removes it. For fewer capabilities delete `.cap` cells and change
`grid-template-columns:repeat(N,1fr)`.

**6. Headline + kicker + tagline.** `.kick` is the "BREAKING NEWS" caps kicker with
flanking gradient rules. `h1` is the big 2-line Poppins headline — wrap the second line
(or the emphasis phrase) in `<span class="g">` for the mint→cyan→blue gradient. `.sub`
is the caps positioning line with flanking rules. `.tag` is the centered caps tagline
above the footer. Keep the headline to 2 lines.

**7. Size.** Near-square `1080×1150` (the source is slightly taller than square, to fit
all bands). Dropping `data-proof="off"` and/or `data-caps="off"` frees height — consider
`1080×1080` then. Change `--w/--h` AND `--window-size` together.

**8. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted merger-announcement
poster. SHIP THE LAYOUT, NOT THE WORDS: the two brand names/logos, headline, all stat
numbers + labels, proof lines, capabilities, tagline, and handle stay neutral
placeholders ("Brand A", "Metric one", "N of Top M"). Never paste the source's real
company names, logos, statistics, or copy into the template or a generated post.

---
