## Tuning graded-compare

A scored before/after. The TWO ARTIFACT CARDS + their score GAUGES are the
identity; the headline and CTA frame them. Portrait `1080×1350` by default. All
adaptation is markup edits + three `data-*` knobs — never a second template.

**1. Artifact cards (`data-art` on `<body>`).** The source's two panels are
document SCREENSHOTS, which can't be generated here. So:
- `css` (default) — each card shows a neutral CSS "document" fallback: the BEFORE
  card is a sparse single-column doc (`.doc`); the AFTER card is a richer
  two-column doc with accent rows (`.doc2`). The asymmetry IS the message — the
  after reads as the upgraded version. Both docs are `flex:1` so they fill the
  card top-to-bottom (don't let them go hollow — add `.ln`/`.bar` rows if a card
  looks empty; this was the build fix).
- `image` — each card becomes a `background-image` slot (`.art`). Drop real
  before/after screenshots by setting `background-image` on `.before .art` and
  `.after .art`. Use this for delivery when you have the actual artifacts; the CSS
  docs auto-hide. Never claim to have rendered a real screenshot.

**2. Score gauges (`data-gauge` on `<body>`).** `on` (default) shows the two
conic-gradient rings below the cards; `off` hides them (collapses to a plain
artifact before/after — but then consider `before-after` instead, since the gauge
is this archetype's reason to exist). Each ring's value is set by the `--p`
percentage in `.before .ring` / `.after .ring` (default 45 / 90); change BOTH the
`--p` and the printed `.num` to keep them in sync (the number is plain text, not
derived). The before ring uses the red `--bad`, the after the green `--good`. The
`.lab` (Low/High) and `.strength` metric chip are free text — relabel to the
metric being scored (e.g. "Resume Strength", "SEO Score", "Audit").

**3. Pills + connector.** Each card is capped by a `.pill` (BEFORE red / AFTER
green). A round `.mid` connector with a Lucide arrow sits between the two cards
(absolute-centered over `.comparezone`); it reinforces before→after. Keep the
pills to one word.

**4. CTA (`data-cta` on `<body>`).** `on` (default) shows the dark CTA pill at
the bottom (Lucide sparkle + label); `off` removes it. One action only — edit the
label, don't add a second CTA.

**5. Headline.** `h1` is a centered 2-line Poppins headline; wrap the benefit
phrase (usually the second line) in `<span class="hl">` for the green accent.
Keep it to 2 short lines — it sits above the cards.

**6. Size.** Portrait `1080×1350` (matches the source). The two tall cards need
the height; don't go square unless you also shrink the cards (`aspect-ratio`) and
the gauges. Change `--w/--h` AND `--window-size` together if resizing.

**7. CONTENT IS STRUCTURE-ONLY.** Distilled from a real, copyrighted before/after
promo. SHIP THE LAYOUT, NOT THE WORDS: the headline, brand mark, gauge numbers,
metric labels, and CTA stay neutral placeholders. The CSS document fallbacks are
abstract bars — never reproduce the source's actual document content, brand, or copy
in the template or a generated post.

---
