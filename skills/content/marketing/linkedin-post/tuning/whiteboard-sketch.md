## Tuning whiteboard-sketch

One template, several optional bands. Build the poster by KEEPING the bands you
need and deleting the rest — never make a second template per band combination.

**1. Bands are independent `<section>` blocks.** In order: title (always),
`.cols` (3-column band, the workhorse), `.mid` (checklist + mini table), `.results`
(icon-stat row), `.callout` (mantra box + takeaway). Delete any `.mid`/`.results`/
`.callout` section the post doesn't need; the layout reflows. The `.cols` band
gives this archetype its identity — keep it.

**2. The 3 columns are heterogeneous on purpose.** Unlike comparison-columns
(uniform cards), each column here can hold different content: prose `<p>`, an
icon-`.flow` of steps, or a plain icon-list. Mix them to match the source's
"challenge / approach / stack" rhythm. Keep each column to ≤ 5 items.

**3. Canvas is taller — `1080×1480` default** (it carries up to 4 bands). Set
`--w/--h` in the palette block AND `--window-size=1080,1480` in the render
command — change both or it crops. If you drop to just title + `.cols` +
`.callout`, shrink to `1080×1080`; document is not a fixed size, it follows band
count.

**4. The hand-drawn look is a CSS approximation, not real art.** Handwriting
fonts (Caveat display / Architects Daughter body), a CSS paper grid, sketchy
double borders (`.sketch`), and marker-tinted **hand-drawn line icons** from the
Iconify `streamline-freehand` set (their wobbly stroke matches the marker medium
— don't use clean Lucide here). It does NOT and cannot produce true hand-drawn
doodles or 3D marker icons — that needs an external illustration tool. Don't
claim otherwise. If the user wants real doodle art, hand them a prompt-recipe:

> "Hand-drawn marker sketchnote on white paper, [subject], blue/purple/green/teal
> marker, doodle icons, slightly imperfect strokes, top-down photo." — adjust
> subject per post.

**5. Content density.** Title takes up to 3 multi-marker words (`.a .b .c` +
`.plus`). The mini table holds ~5 rows comfortably; the stat row is 3–5 icons
(edit the `.stats` `grid-template-columns` count to match). Keep handwriting
copy short — handwriting fonts eat horizontal space and wrap fast; one short
clause per line.

**6. Picking freehand icons (gotcha).** `streamline-freehand` names are verbose
and inconsistent (no `github`; `key` resolves to `keyboard`; `code` to a bitcoin
glyph). Don't guess — search the set and VERIFY a name resolves before using it:
`https://api.iconify.design/streamline-freehand.json?icons=NAME1,NAME2` returns
`not_found: []` when all exist. A missing name renders as a blank gap, not an
error. Tint each icon with its section's marker accent (already wired via the
`.c1/.c2/.c3` and `.stat:nth-child` rules).

**7. Match the source mood, not house style.** This template defaults to its
ink-on-paper marker theme per the reference-matching rule. A different sketchnote
reference → re-sample its marker hex into the palette block rather than reusing
these exact colors.

---
