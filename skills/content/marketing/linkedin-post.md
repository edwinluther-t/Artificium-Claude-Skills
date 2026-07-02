---
name: linkedin-post
description: Generate LinkedIn infographic graphics plus post copy. Picks an archetype, applies a palette and font pairing, renders a LinkedIn-sized PNG via headless Chrome from a bundled HTML template, and writes hook-first copy. Use when the user wants a LinkedIn post, carousel slide, infographic, or branded diagram for LinkedIn.
---

# LinkedIn Post

Turn an idea into a LinkedIn-native graphic + copy. Self-contained: archetype
library, twenty-four HTML templates, palettes, font pairings, and a render pipeline
all ship with this skill. Fonts and icons load from CDN at render time (no
binaries bundled) — only requirement is network during the Chrome render.

This skill inherits copy discipline from `content-engine`: one claim, hook
first, no hype, no reply-bait, no emoji-spam.

---

## Layout rules (read first — these are non-negotiable)

**Rule #1 — A template's DEFAULT layout MUST match the layout of the reference
image it was distilled from.** The full structure the source shows is the
default the template ships and renders out of the box — not a reduced subset.
If the source has a left rail + center map + right rail, the template's default
`data-*` state shows all three. Do NOT default to a trimmed version and make the
user opt back into what the original already had. (This is the rule that was
violated repeatedly while building `architecture-map`: it defaulted to
right-rail-only when the source clearly had both rails.) When you build or edit a
template, render the DEFAULT state and compare it to the reference — they must
match structurally before you ship.

**Rule #2 — Layout is adjustable at apply-time.** The default matches the source,
but the user (or the AI applying this skill) can change it per need: switch
`data-*` modes, drop/add bands or rails, change orientation/size, recolor. Every
adjustable knob is documented in the relevant "Tuning <archetype>" section below.
When applying the skill: start from the source-matching default, then adapt only
what the specific post needs.

**Rule #3 — Replace the footer brand mark with the END-USER's details.** Every
template ships a `.foot` row hardcoded with the kit author's mark
(`The Artificium` / `@edwinluther-t`). This is a placeholder default, NOT a fixed
credit. Before delivering any generated graphic, the applying AI MUST replace it
with the end-user's own brand + handle (or remove the `.foot` row entirely if they
want no footer). Never ship a post carrying the kit author's name/handle as if it
were the poster's — ask the user for their brand/handle if not given, or leave the
footer blank.

---

## Workflow

1. **Get the message.** One sentence: what is the single thing this post says?
   If the user gave a topic but not a claim, draft the claim and confirm.
2. **Pick the archetype** (decision tree below). State which and why in one line.
   If a secondary beat needs a block the base doesn't carry, decide the hybrid
   here: name the base + the block(s) to graft (see Hybrid posts below).
3. **Pick size.** Portrait `1080×1350` is the LinkedIn default (most feed real
   estate). Use landscape `1200×627` for link-preview-style or pipeline graphics.
4. **Pick palette + type.** Default is the house dark-tech theme. Offer one
   alternate if the topic clashes (see Palettes).
5. **Fill the template.** Copy the chosen template, edit the data in the markup,
   swap palette vars / fonts if changing theme. If hybridizing, graft the
   borrowed block(s) here and restyle them to the base palette.
6. **Render** (pipeline below) to `$TEMP`, then `mv` into the target dir.
7. **Write the copy** (Copy rules below): hook, body, optional list, soft CTA.
8. **Deliver** the PNG path + the copy block. If photoreal/3D was requested, see
   the Scope limits branch — do not fake it.

---

## Decision tree (intent → archetype)

```
Is the post built around ONE big number?              → stat-banner
Comparing OLD process vs NEW process?                 → before-after
Busting a misconception (belief vs fact)?             → think-vs-reality
A left-to-right process / handoff across stages?      → role-pipeline
A system shown as horizontal layers (UI→data)?        → layered-stack
One central thing connected to several parts?         → hub-and-spoke
A reference list of many small equal items?           → cheatsheet-grid
Placing something on a progression / levels?          → maturity-scale
3-4 named components that COMBINE into one system?    → comparison-columns
Two PEER concepts compared across matched attributes? → versus-list
A MULTI-SLIDE carousel / document post (deck)?        → carousel-slide
A dense hand-drawn "sketchnote on paper" explainer?   → whiteboard-sketch
A SYSTEM diagram — boxes connected by arrows?         → architecture-map
A LAYERED system with DATA FLOWING along connectors?  → animated-flow-map
Announcing an open role / "we're hiring" / join us?   → hiring-banner
Promoting a downloadable asset (guide/ebook/factsheet)? → lead-magnet-promo
Promoting an EVENT (webinar/summit/series) — register?  → event-banner
Announcing a PERSON (new hire/appointment/promotion)?   → person-spotlight
An article/blog/link COVER — headline over a hero scene? → cover-hero
Two CHARTS contrasted (sparse vs diversified, as data)?  → chart-compare
A weak ARTIFACT vs an upgraded one, each SCORED by a meter? → graded-compare
A whole-topic reference POSTER of many MIXED panels (a wall)? → cheatsheet-wall
Announcing a PARTNERSHIP/MERGER of TWO brands (A × B)?   → partnership-banner
Several STACKED left→right pipelines w/ moving direction dots? → layered-loop-map
```

Note: `carousel-slide` is a different kind of output — a SLIDE SYSTEM, not a
single image. The others are one-shot infographics; carousel-slide renders one
slide per pass and you assemble a deck. Pick it when the user wants a "carousel",
"document post", "swipe", or a numbered multi-page narrative.

Tie-breakers:
- Process vs belief: `before-after` is *how the work changes*; `think-vs-reality`
  is *what's true*. If no process changes, it's think-vs-reality.
- `hub-and-spoke` vs `layered-stack`: spokes are peers around a center; layers
  are ranked top-to-bottom. If order matters, use layers.
- `architecture-map` vs `role-pipeline` vs `hub-and-spoke`: all three connect
  boxes, but — pipeline is a LINEAR left→right stage flow (no branches);
  hub-and-spoke is RADIAL peers around one center; architecture-map is a DIRECTED
  graph (top-down flow that branches/fans out, with optional side rails). If the
  system has branches or sub-systems, it's architecture-map.
- `architecture-map` vs `animated-flow-map`: both are connected system diagrams.
  architecture-map is STATIC (a wide directed graph, icon-list rails).
  animated-flow-map is a TALL stack of numbered LAYERS with DATA FLOWING along the
  connectors (CSS-animated dots) + a numbered-takeaways rail. Pick it when motion
  (flow/data movement) is part of the story, or for a dense 5-layer top-down stack.
- `animated-flow-map` vs `layered-loop-map`: both are the ANIMATED archetypes (moving
  flow dots) — pick by TOPOLOGY. `animated-flow-map` is ONE top-down stack: dots flow
  DOWN a single trunk between numbered layer bands, framed by a left tier-rail + a
  right takeaways-rail. `layered-loop-map` is SEVERAL independent HORIZONTAL pipelines:
  each colored "Layer N" band is its own left→right box chain and dots flow SIDEWAYS
  within it; it's led by an optional two-panel VS comparison header and closed by a
  maturity-scale chevron row + CTA. If the story is "one system, data flows down the
  layers" → animated-flow-map; if it's "several progressive layers, each a left→right
  process, with a compare header" → layered-loop-map. (Both share the same flow-dot
  animation + the bundled `make_flow_gif.py` GIF pipeline.)
- More than ~9 items → `cheatsheet-grid`. Fewer with a center → hub-and-spoke.
- `cheatsheet-grid` vs `cheatsheet-wall`: both are savable references, but
  `cheatsheet-grid` is a UNIFORM grid of EQUAL tiles (one shape: icon + code +
  desc), good for a flat list of many similar items (shortcuts, commands, tips).
  `cheatsheet-wall` is a dense MASONRY POSTER of HETEROGENEOUS panels of different
  sizes and inner content types (a code block, a mini flow diagram, a file-tree, a
  layered stack, compare columns, a command list) covering a whole topic, with a big
  two-tone title and a footer CTA band. If the items are all the same kind → grid; if
  it's "everything about X" mixing several content formats → wall.
- Two-column disambiguation: `before-after` = old vs new PROCESS (one is worse);
  `think-vs-reality` = belief vs fact, ONE statement each; `versus-list` = two
  PEER concepts each with a matched icon-list of attributes (both valid).
- The ANNOUNCEMENT archetypes (all = headline + CTA, differ by what they
  promote): `hiring-banner` = an OPEN role ("apply"; skills/expertise band + hero
  art slot, landscape); `person-spotlight` = a FILLED role / a PERSON ("X joins as
  ROLE"; hero portrait + bio icon-list + quote + engagement bands, square);
  `event-banner` = an EVENT (date/format meta + a right-side icon-badge cluster);
  `lead-magnet-promo` = a DOWNLOADABLE asset (benefit list + an asset COVER render);
  `partnership-banner` = a PARTNERSHIP/MERGER of TWO brands (an "A × B" two-logo
  lockup + combined-scale stat row + proof strip, cinematic hero, dark).
  Pick by the object promoted. Open vacancy → hiring-banner; a named person already
  appointed → person-spotlight; two brands combining → partnership-banner.
- Comparison family: `before-after`/`think-vs-reality`/`versus-list` are TEXT/icon
  columns; `chart-compare` is the one where the contrast is carried by two DATA
  CHARTS (a sparse pie vs a dense radial bar-fan). If the message is "look at the
  visual difference between these two charts", use chart-compare; if it's lists of
  attributes/statements, use a text-column one.
- `before-after` vs `graded-compare`: both contrast an old vs an improved version,
  but `before-after` compares TEXT bullet lists (friction points vs wins), while
  `graded-compare` compares two visual ARTIFACTS (a document/screen/profile shown
  as a card) each given a NUMERIC SCORE by a circular gauge, plus a CTA. If the two
  things being compared are images/artifacts that get rated, use graded-compare; if
  they're lists of points, use before-after.

---

## Hybrid posts (borrow blocks into a base)

Archetypes are not mutually exclusive. The decision tree picks the BEST single
fit, but a post often reads stronger as a considered blend — a base archetype
with one or two self-contained blocks grafted in from another. This is
encouraged; use it when the message has a secondary beat the base template
doesn't natively carry (a headline number, a progression, a closing CTA band, a
side rail of items).

**The rule: one BASE, borrowed BLOCKS.**

1. **Pick one base archetype** (via the decision tree, as normal). The base owns
   the CANVAS SIZE, the PALETTE, the FONTS, and the single `.foot` row. These are
   decided once, by the base, and never mixed. A hybrid is still ONE rendered PNG
   with ONE coherent look.
2. **Graft a block, not a template.** A "block" is a self-contained horizontal
   band or a side rail that carries one idea. Copy that block's MARKUP out of the
   donor template, paste it into the base's `.wrap`, then **restyle it to the
   base's palette vars** — donor class names and colors do NOT carry over (each
   template has its own private class vocabulary; there is no shared component
   system). You are transplanting structure, then re-skinning it. Keep the base's
   `--bg/--ink/--accent`; drop the donor's.
3. **Keep it to 1–2 grafts.** A base + one hero stat + one CTA band reads clean.
   Four borrowed blocks is not a hybrid, it's a mess — if you need that many, you
   picked the wrong base (or it's genuinely a `cheatsheet-wall`, which is the
   archetype whose whole job is heterogeneous panels — reach for that instead of
   hand-building a wall).
4. **Respect the layout rules.** Rule #1 (default matches source) applies to the
   BASE. Grafted blocks are an apply-time adaptation (Rule #2) — they're additive
   customization for this specific post, not a change to the base template's
   shipped default. Don't edit the base `.html`; compose in your working copy.
5. **Render and look.** Grafting breaks vertical rhythm more often than any other
   edit — a transplanted band fights the base's spacing/flex. Give the base's main
   region `flex:1` so the graft doesn't leave dead space, and re-render until the
   seams disappear. Judge the composite as one image.

**Reusable blocks worth borrowing (donor → what it adds):**

| Block | From | Adds |
|---|---|---|
| Giant hero numeral | `stat-banner` | one headline metric above/below the base |
| Chevron progression row | `maturity-scale` | a "where this sits on a scale" closer |
| Full-width CTA band | `lead-magnet-promo` / `partnership-banner` / `cheatsheet-wall` | a strong bottom call-to-action |
| Icon-list side rail | `architecture-map` / `animated-flow-map` | a "principles / tools / takeaways" column |
| ✓/✗ checklist column | `comparison-columns` / `think-vs-reality` | a do/don't or has/lacks list |
| Proof / stat strip | `partnership-banner` | a row of 3–5 supporting numbers |
| Engagement band | `person-spotlight` | a Like/Comment/Share/Follow footer strip |
| Quote band | `person-spotlight` | a pulled-quote value statement |

**When NOT to hybridize:** if a single archetype already carries the whole
message, ship it plain — don't graft for its own sake. And never blend two BASES
(two canvases, two palettes) into one image; that's the mess Rule #1 exists to
prevent. Borrow blocks INTO a base; never fuse two bases.

If you borrow from an archetype that has a `tuning/<archetype>.md`, skim that
file for the block you're taking — it documents that block's `data-*` knobs and
sizing so the graft behaves.

---

## Archetype library

Each template lives in `templates/<archetype>.html` next to this file. They are
self-contained pages with a 5-variable palette block, CDN fonts, CDN icons, and
placeholder data to replace.

| Archetype | When | Layout logic | Default icon set |
|---|---|---|---|
| hub-and-spoke | 1 core + 3–6 parts | 2 layouts: centered (title above a centered hub, house dark) · split (left title-block + right 6-node ring w/ dashed connector + bottom stat strip, light-indigo) | lucide |
| before-after | old vs new process | 2 panels, red→green | lucide |
| think-vs-reality | myth vs fact (belief vs reality) | 3 layouts: minimal (1 statement/side, dark) · rich-divider (icon-grid + ✓/✗ list, center line, light green/red) · rich-image (adds hero image slots) | lucide (minimal) / streamline-freehand (rich) |
| role-pipeline | staged flow | columns + arrows | lucide |
| layered-stack | system layers | stacked bands top→down | lucide |
| cheatsheet-grid | many small items | 2×N tile grid | lucide |
| stat-banner | one big number | giant numeral hero | lucide |
| maturity-scale | levels / progression | ascending bars + row | lucide |
| comparison-columns | 3–4 components that combine into one system | accent-coded cards: icon → checklist → Output box, + summary banner | lucide |
| versus-list | two peer concepts, matched attributes | 2 columns of icon → label rows, center VS badge / image slot, payoff banner | lucide |
| carousel-slide | a multi-slide carousel/document post | one slide per render; modes: cover / list / statement; dark-neon glass; next-cue + counter | lucide |
| whiteboard-sketch | a whole-topic hand-drawn explainer poster | marker title + 3 annotated columns, then optional bands: checklist + mini table, icon-stat row, key-learning callout; paper grid, handwriting type, sketchy borders | streamline-freehand |
| architecture-map | a connected SYSTEM/architecture diagram | center column of labeled nodes joined by CSS arrows (vertical flow + flank triple + fan-out row) + optional side rail(s) of category panels + bottom banner; landscape | lucide |
| animated-flow-map | a dense layered system with ANIMATED flow dots | left numbered tier rail + center stack of connected layer bands (CSS flow dots travel along connectors) + right numbered-takeaways rail + social footer; portrait-tall; live HTML animates, exports still PNG or a PIL-stitched looping GIF | lucide |
| hiring-banner | an open-role / "we're hiring" / join-us announcement | hero band (badge → big role title → tagline + art slot) over a 3-zone info band: core-skill column + secondary expertise column + value-prop callout ending in a DM/CTA chip; landscape | lucide (chrome only) + art slot |
| lead-magnet-promo | promoting a downloadable resource (guide/ebook/factsheet/checklist) | left column: muted+bold 2-part title → N benefit rows (badge icon + 2-line label) → glowing CTA pill; right column: a tilted lead-magnet COVER card on a CSS pedestal (logo → image slot → tag → title → subtitle → URL); portrait | lucide + cover image slot |
| event-banner | promoting an event (webinar/summit/conference/virtual series/workshop) | left: logo lockup → big 2-line event title → tagline → meta line (format · sessions / dates) → dark CTA pill; right: a curved swoosh panel holding a grid of circular icon badges (filled) + outlined info chips; landscape | lucide |
| person-spotlight | announcing a person (new hire / senior appointment / promotion / award) | left: eyebrow → big gradient headline → "name joins ORG as ROLE" sub → N bio icon-rows; right: hero PORTRAIT image slot w/ CSS chip-glow ring + name plate; bottom full-width: quote band + Like/Comment/Share/Follow engagement band; square | lucide + portrait image slot |
| cover-hero | an article / blog / link COVER (headline over a hero scene) | full-bleed background (self-contained sci-fi CSS scene: gradient + perspective grid + glowing connector-node network — OR a supplied image) → legibility scrim → kicker chip → big 2–3 line gradient headline → meta/footer row; landscape | lucide |
| chart-compare | a two-up CHART comparison (the message is the visual difference) | logo → big headline → two side-by-side CSS charts (LEFT sparse conic-gradient pie · RIGHT dense radial bar-fan wheel), each with caption + verdict line → CTA pill; square | lucide (verdict/CTA only) + CSS charts |
| graded-compare | a weak vs upgraded ARTIFACT, each scored | logo → 2-line headline (accent 2nd line) → two artifact cards (CSS document fallback or image slot), each capped by a BEFORE/AFTER pill and scored below by a conic-gradient gauge + metric chip, center connector arrow → dark CTA pill; portrait | lucide (arrow/CTA) + CSS gauges + artifact image slots |
| cheatsheet-wall | a dense whole-topic reference POSTER of mixed panels | big two-tone title + logo → CSS-column masonry of heterogeneous .panel blocks (code block · mini flow diagram · file-tree · layered funnel-stack · compare columns · full-width command list), each with a blue header bar → full-width purple CTA band + footer; portrait-tall | lucide (sparse) + CSS code/tree/funnel |
| partnership-banner | announcing a partnership / merger of TWO brands | BREAKING-NEWS kicker → two-logo "A × B" lockup (icon+wordmark, swappable to logo images) → gradient 2-line headline → subhead → cinematic hero band (image slot / CSS glow) → 4–5 icon+stat cells → "N of TOP M" 3-cell proof strip → 6-icon capability strip → tagline footer; near-square dark | lucide + logo image slots + hero image/CSS |
| layered-loop-map | several stacked left→right pipelines with ANIMATED direction dots | two-tone title + subhead → optional two-panel VS comparison header (+ VS badge) → 3–4 stacked colored "Layer N" bands, each a left→right chain of boxes joined by connectors carrying moving flow dots → maturity-scale chevron row → CTA band + footer; portrait-tall; live HTML animates, exports still PNG or a PIL-stitched looping GIF | lucide + CSS flow dots |

`comparison-columns` (themed after a "tool-stack combo" infographic) defaults to
the **light multi-accent** palette (each column owns a color), not the house
dark-tech theme. See "Tuning comparison-columns" below — it is the one template
that needs sizing decided per content.

`versus-list` (themed after an "A vs B" comparison infographic) defaults to the
**soft light purple/blue** palette. It has two center-zone modes
(`<body data-center>`): `divider` (clean VS badge, renders here) and `image` (a
slot for a supplied illustration). See "Tuning versus-list" below.

`carousel-slide` (themed after a multi-slide "document post" deck) is a SLIDE
SYSTEM: one template with `data-slide` modes (`cover` / `list` / `statement`) on
a shared **dark-neon glass** theme. Render one slide per pass; build the full
deck by editing data + slide mode and re-rendering each page. See "Tuning
carousel-slide" below.

`whiteboard-sketch` (themed after a hand-drawn marker whiteboard explainer
poster) defaults to the **ink-on-paper marker** palette and handwriting type. It
is a multi-BAND poster: a marker title, a 3-column annotated band, then any of an
optional checklist + mini metrics table, an icon-stat results row, and a
key-learning callout — drop the bands you don't need. Its value is the MEDIUM, so
it is a true CSS approximation of marker-on-paper, NOT real hand-drawn art (see
"Tuning whiteboard-sketch" below). It is taller than the others (`1080×1480`) to
hold the bands.

`think-vs-reality` is a MODE-TOGGLED template with three layouts (set on
`<body data-layout="...">`): `minimal` (the original — one statement per side, on
the house dark-tech theme), `rich-divider` (each side gets an icon-grid + a ✓/✗
list split by a center divider line, light green-vs-red theme), and `rich-image`
(same rich content but each side leads with a hero image slot). The two rich
modes are themed after a denser "what people think vs what it actually involves"
explainer and use hand-drawn `streamline-freehand` icons. See "Tuning
think-vs-reality" below.

`architecture-map` (themed after a connected full-stack architecture diagram)
defaults to a **clean light flat-tech, multi-accent** palette and is LANDSCAPE
(`1350×1080` — architecture reads wide). The center map is labeled nodes joined
by CSS arrow connectors (a vertical trunk, a flanking "triple", and a fan-out
row); side rails and box counts are knobs. Uses clean flat Lucide icons (the
medium is flat-tech — NOT the hand-drawn freehand set). See "Tuning
architecture-map" below.

`animated-flow-map` (themed after a dense "enterprise system architecture"
explainer) is a TALL portrait stack (`1080×1500`) of numbered LAYER bands joined
by connectors that carry **CSS-animated flow dots** (source→destination, looping),
framed by a left numbered tier rail and a right numbered-takeaways rail. It is the
ONLY animated archetype: the HTML animates live in a browser; this machine exports
a still PNG (one frame) OR a looping GIF stitched from phase-stepped frames with
PIL (no ffmpeg here). See "Tuning animated-flow-map" below for the GIF workflow.

`hub-and-spoke` is MODE-TOGGLED (`<body data-layout="...">`): `centered` (the
original — eyebrow + title stacked above a centered hub, house dark-tech,
portrait `1080×1350`) and `split` (DEFAULT — a left title-block beside a right
radial RING of 6 nodes around a glyph+label hub joined by a dashed connector,
plus a bottom 3-cell stat strip; light-indigo theme, landscape `1200×760`). The
`split` layout is themed after a "resource hub" marketing infographic. See
"Tuning hub-and-spoke" below.

`hiring-banner` (themed after a dark-navy "we're hiring" role poster) defaults to
a **dark navy / electric-blue with a yellow badge** palette and is LANDSCAPE
(`1200×750`). It is an announcement, not a diagram: a hero band (badge → big
2-line role title → tagline + a hero art slot) over a 3-zone info band — a primary
skill checklist, a secondary expertise column, and a value-prop callout that ends
in a "DM me / interested?" CTA chip. The hero art slot defaults ON (the source's
glossy 3D illustration can't be generated here — supply real art or use the
prompt-recipe; do NOT substitute clip-art icons). See "Tuning hiring-banner" below.

`lead-magnet-promo` (themed after a "download my factsheet/guide" resource promo)
defaults to a **purple-lilac gradient with a mint CTA** palette and is PORTRAIT
(`1080×1350`). It is a download-driver: a left column (muted+bold split title → a
list of benefit rows, each a round badge icon + 2-line label → a glowing pill CTA)
beside a right column holding a tilted lead-magnet COVER card on a CSS pedestal
(logo → image slot → tag → title → subtitle → URL). The cover's photographic hero
and the source's glossy 3D device CANNOT be generated here: the cover defaults to a
flat CSS card with an image slot (`data-cover="card"`); supply real art or use the
prompt-recipe — do NOT fake a 3D mockup. See "Tuning lead-magnet-promo" below.

`event-banner` (themed after a sky-blue event-promo banner) defaults to a
**sky-blue with dark-circle badges** palette and is LANDSCAPE (`1200×627` — the
LinkedIn link-preview banner ratio). It is an event announcement: a left column
(logo lockup → big 2-line event title with a dark/white split → tagline → a meta
line of format · sessions / dates → a dark CTA pill) beside a right curved swoosh
panel holding a 3×N grid of circular icon badges — filled dark-circle icon badges
plus outlined white "info chips" (e.g. LIVE / LEVEL / LABS). All flat Lucide,
fully renderable (no image slot). See "Tuning event-banner" below.

`person-spotlight` (themed after a dark AI-appointment poster) defaults to a
**near-black with a blue→violet gradient headline** palette and is SQUARE
(`1080×1080`). It announces a PERSON (a senior appointment, new hire, promotion,
or award — the role is FILLED, unlike `hiring-banner`'s open vacancy): a left
column (eyebrow → huge gradient headline → "name joins ORG as ROLE" sub-headline →
a vertical list of bio icon-rows with accent keywords), a right hero PORTRAIT image
slot (defaults ON) carrying a CSS chip-glow icon ring + a name/title plate, and two
full-width bottom bands — a quote value-prop band (quote mark + statement + logo)
and an engagement band (follow prompt + Like/Comment/Share/Follow). The portrait
can't be generated here — supply real art or use the prompt-recipe; the chip ring,
plate, and bands are all CSS/Lucide. See "Tuning person-spotlight" below.

`cover-hero` is an article/blog/link COVER — a bold multi-line headline over a
full-bleed hero. It is the ONE archetype that does NOT copy a source layout: its
reference was almost entirely AI-generated illustration (un-reproducible here), so
instead it ships a self-contained **sci-fi CSS scene** — a deep indigo→teal space
gradient, a perspective grid horizon, a glowing CSS connector-node network (abstract
nodes joined by gradient lines, NOT robots), and neon accents — that stands alone
with no supplied art. Over it sit a legibility scrim, a kicker chip, a big 2–3 line
gradient headline, and a meta/footer row. An image slot (`data-bg="image"`) lets a
real hero photo replace the CSS scene. LANDSCAPE `1200×630` (link-cover ratio).
See "Tuning cover-hero" below. (This is the documented exception to the
reference-matching rule, made at the user's explicit direction for this archetype.)

`chart-compare` (themed after a silver-grey two-up portfolio comparison) defaults
to a **light silver-grey with a red accent + multi-hue charts** palette and is
SQUARE (`1080×1080`). The argument is carried by two REAL CSS charts side by side:
a LEFT sparse conic-gradient PIE (few big slices = concentrated) vs a RIGHT dense
radial BAR-FAN wheel (many small spokes = diversified), each under a caption + a
one-line verdict, with a headline above and a CTA pill below. The source's
photoreal 3D chart renders are NOT reproduced — these are honest flat 2D CSS
charts (conic-gradient + radially-transformed bars), which carry the same
sparse-vs-diversified message without any image dependency. See "Tuning
chart-compare" below.

`graded-compare` (themed after a "weak vs upgraded artifact" before/after promo)
defaults to a **light mint with green accent + red/green gauges** palette and is
PORTRAIT (`1080×1350`). It is a before/after where each side is a VISUAL ARTIFACT
(a document, screen, design, or profile) that gets a NUMERIC SCORE: a logo + 2-line
headline (accent second line) over two artifact cards, each capped by a colored
BEFORE/AFTER pill and scored below by a circular conic-gradient gauge + a metric
chip, a center connector arrow, and a dark CTA pill. The artifact cards default to
a neutral CSS "document" fallback (`data-art="css"` — the before card reads as a
sparse single-column doc, the after card as a richer two-column doc, conveying the
upgrade) with an image slot (`data-art="image"`) to drop in real screenshots. The
source's actual document screenshots and emoji/thumb stickers can't be generated
here — supply real art or use the CSS fallback; do not fake them. Distinct from
`before-after` (which compares TEXT bullet lists, not scored artifacts). See "Tuning
graded-compare" below.

`cheatsheet-wall` (themed after a dense white "everything about X" reference poster)
defaults to a **clean white poster with red/black two-tone title, blue panel headers,
purple CTA band** palette and is PORTRAIT-TALL (`1080×1580` — the wall needs height).
It is a savable WHOLE-TOPIC reference: a big two-tone title + a small logo lockup over
a CSS-column MASONRY of heterogeneous `.panel` blocks — a code block, a mini flow
diagram (3 sub-columns of stacked nodes + arrows), a file-tree, a layered
funnel-stack, a compare-columns block, and a full-width command list — each panel
capped by a blue header bar, over a full-width purple CTA band + footer. Distinct from
`cheatsheet-grid` (a UNIFORM grid of equal tiles): this mixes content TYPES at
different spans. The source's glossy 3D funnel and small illustration can't be
generated here — the funnel is a CSS layered-stack approximation and illustrations are
dropped or replaced with flat Lucide; do not fake the 3D art. Each `.panel` is an
independent block — keep/drop/reorder to fit, set `.span2` for a full-width panel. See
"Tuning cheatsheet-wall" below.

`partnership-banner` (themed after a dark cinematic merger-announcement poster)
defaults to a **near-black cosmic with a mint→cyan→blue gradient headline + orange
accent** palette and is NEAR-SQUARE (`1080×1150`). It announces a PARTNERSHIP / MERGER
/ ACQUISITION / JOINT-VENTURE between TWO brands: a "BREAKING NEWS" kicker → a two-logo
"A × B" lockup (each side an icon-glyph + wordmark, swappable to a real logo image) → a
big 2-line gradient headline → a subhead line → a cinematic hero band → a row of 4–5
icon+stat cells (the combined scale) → a "N of TOP M" 3-cell proof strip → a 6-icon
capability strip → a centered tagline footer. It is a fifth ANNOUNCEMENT archetype,
distinct from the other four by the object promoted (two brands combining) and its
payload (a two-logo lockup + aggregate stats), and distinct from `stat-banner` (ONE
number) by being a multi-stat merger announcement with logos and a hero scene. The
hero defaults to an image slot (`data-hero="image"` — the source's photoreal
earth-from-space glow can't be generated here; supply real art or use the
`data-hero="css"` cosmic-glow fallback), and the two logos default to icon+wordmark
placeholders (swap `.lmark` for real logo images). See "Tuning partnership-banner"
below.

`layered-loop-map` (themed after a light-indigo multi-layer "loop" explainer) defaults
to a **white with per-layer indigo/green/blue/orange accents + a purple CTA band**
palette and is PORTRAIT-TALL (`1080×1400`). It is the SECOND animated archetype: a
two-tone title + subhead → an optional two-panel VS comparison header (two small loop
diagrams + a VS badge) → 3–4 stacked colored "Layer N" bands, each a left→right chain
of boxes joined by connectors that carry **CSS-animated flow dots showing direction** →
a maturity-scale chevron row → a CTA band + footer. It shares the flow-dot animation
technique with `animated-flow-map` but is a DIFFERENT topology: several INDEPENDENT
HORIZONTAL pipelines (dots flow sideways within each band), not one top-down trunk, and
it adds the VS header + maturity row. The HTML animates live in a browser; this machine
exports a still PNG (one frame) OR a looping GIF stitched from phase-stepped frames with
PIL via the bundled `make_flow_gif.py` (now shared by both animated archetypes — pass
the template name). See "Tuning layered-loop-map" below.

**Reference-matching rule:** when a template is distilled from a specific
reference, its DEFAULT palette/type should MATCH that reference, not be forced
into house dark-tech. House style is the default only for the original archetypes
that have no source image.

---

## Palettes (swap the 5 vars at the top of any template)

House dark-tech is the default. Each palette = `--bg --panel --line --ink
--muted --accent`.

- **dark-tech (default):** `#0a0a0b #141416 #26262b #f4f4f5 #a1a1aa #f5a623`
  — dev/AI/infra topics. Amber accent. The Artificium house style.
- **clean-light:** `#ffffff #f4f4f5 #e4e4e7 #18181b #52525b #2563eb`
  — business/strategy, broad audiences. Blue accent.
- **deep-violet:** `#0d0a18 #181230 #2a2350 #f5f3ff #a99fd6 #8b5cf6`
  — product/design/creative. Violet accent.
- **forest:** `#0a0f0b #121a14 #233028 #f0fdf4 #9fb8a8 #22c55e`
  — growth, sustainability, finance-green.
- **light multi-accent** (default for `comparison-columns`): white bg
  `#ffffff`, ink `#15152b`, muted `#5b5b73`, green-check `#16a34a`, and four
  per-column accents `--c1 #16a34a --c2 #7c3aed --c3 #2563eb --c4 #0f766e`.
  — tool/stack combos, "X + Y + Z" posts. Reads as bright and editorial.
- **soft light purple/blue** (default for `versus-list`): bg `#f7f5ff`, panel
  `#ffffff`, line `#e7e3f7`, soft `#efeafd`, ink `#2a2350`, muted `#6a6390`,
  left accent `#4f46e5` (indigo), right accent `#9333ea` (violet). Rounded,
  friendly. — "A vs B", comparison, approachable/community topics.
- **dark-neon glass** (default for `carousel-slide`): bg `#06080a`, panel
  `#10151b`, line `#1e2a33`, ink `#eaf2f5`, muted `#90a3ad`, with three accents
  teal `#37e0c4`, green `#7CFFB2`, gold `#f4c14b`. Glass panels (inner
  highlight + soft shadow), radial glows, neon text. — agent/AI/infra carousels,
  premium "deck" feel. High-contrast, looks expensive on the feed.

- **ink-on-paper marker** (default for `whiteboard-sketch`): warm paper bg
  `#fbfaf5`, paper2 `#f3f1e7`, grid line `#e7e3d4`, ink `#1f2a4a`, muted
  `#5a5f70`, border `#c9c4b2`, with six marker accents blue `#2f5fd0`, purple
  `#7c3aed`, green `#1f9e57`, amber `#e0922f`, red `#d8483f`, teal `#0f8f88`. A
  faint grid is drawn as a CSS background; sketchy double borders + handwriting
  fonts carry the marker feel. — sketchnote explainers, "whiteboard teardown"
  posts, dense whole-topic overviews. Reads warm, human, hand-made.

- **clean light flat-tech** (default for `architecture-map`): bg `#f6f7fb`,
  panel/node `#ffffff`, line `#dfe3ee`, node-line `#c9d0e4`, ink `#1d2230`, muted
  `#5c6480`, arrow/connector `#9aa3c0`, with six section accents blue `#2f6df0`,
  violet `#7c3aed`, green `#16a34a`, red `#e0483f`, teal `#0f8f88`, amber
  `#e0922f`. Faint dotted grid bg. — architecture/system diagrams, technical
  "how it fits together" posts. Reads clean, corporate-technical.

- **light multi-layer** (default for `animated-flow-map`): bg `#f7f8fb`, panel
  `#ffffff`, line `#e3e7f0`, ink `#1b2138`, muted `#5b6280`, title accent orange
  `#e0532a`, connector `#c7cfe2`, and five per-layer accents L1 `#3b5bd9` (blue),
  L2 `#7c4dd6` (violet), L3 `#2f9e57` (green), L4 `#e0822f` (amber), L5 `#3aa0c8`
  (cyan). Flow dots inherit each connector's layer accent. — dense layered system
  / "how the whole pipeline flows" posts. Reads clean, technical, energetic.

- **light-indigo** (default for `hub-and-spoke` split layout): bg `#f4f6fc`,
  panel `#ffffff`, line `#e3e8f5`, ink `#141a3a`, muted `#5d6485`, accent indigo
  `#4f57f5`, accent2 `#7b6cf6`, dashed connector `#c4ccea`, hub-ring `#eef0fd`.
  Clean, bright, SaaS-deck feel. — "resource hub" / "everything for X" posts,
  product ecosystems, capability maps. (The house dark-tech palette remains the
  default for hub-and-spoke's `centered` layout.)

- **dark navy / electric blue** (default for `hiring-banner`): bg gradient navy
  `#0a1838`→`#0a1430`, panel `#0f2450`/`#102a5e`, line `#244183`, ink `#ffffff`,
  muted `#9db4e0`, accent blue `#2f7bff`, highlight `#56a4ff`, yellow badge
  `#f5c518`, green check `#2fd07a`. Faint masked circuit grid. — hiring posts,
  role announcements, "join us". Reads corporate-energetic, recruiter-grade.

- **silver-grey / red + multi-hue** (default for `chart-compare`): bg radial
  `#e9e9eb`→`#dededf`, ink `#171717`, muted `#5a5a5e`, line `#cfcfd2`, red accent
  `#d92027` (headline emphasis + CTA), hub `#e7e4dc`. Sparse-pie accents green
  `#5bbf2a` / orange `#e8821e` / yellow `#f0c419` / olive `#7a9e1f`; dense-wheel
  spectrum adds blue `#3f8ddb`, red, teal-green `#2f7d4f`, bronze `#b8862f`, purple
  `#6b4ea8`. — data-driven comparison posts (portfolio/allocation/before-after as
  charts). Reads clean, corporate, infographic.

- **sci-fi neon** (default for `cover-hero`): deep space gradient indigo
  `#0a0f2c`→teal `#0d2438`→`#10183a`, with layered radial glows in violet
  `#7c5cff`, cyan `#22e3d6`, and magenta `#ff4fd8`; ink `#ffffff`, muted `#9fb4d8`,
  grid line `rgba(80,150,220,.16)`. Headline uses a cyan→violet→magenta gradient
  clip. — article/blog/link covers, cinematic AI/tech hero posts. Reads premium,
  futuristic, high-energy. (This palette is self-contained CSS art, not sampled
  from a reference.)

- **near-black / gradient-headline** (default for `person-spotlight`): bg radial
  `#11162e`→`#080a14`, panel `#0d1020`, line `#1e2440`, ink `#ffffff`, muted
  `#9aa3c4`, headline gradient blue `#4d7cff`→violet `#9a6cff`, keyword accent
  `#5b8cff`, badge ring `#2f3a66` with `#bcd0ff` icon, chip-glow `#3a6cff`. —
  person / appointment / new-hire spotlight posts. Reads premium, corporate-tech,
  high-contrast.

- **sky-blue / dark-badge** (default for `event-banner`): bg `#5aa6e0`, swoosh
  `#7cbceb`, ink `#10141a`, ink-soft `#1c2733`, muted `#23425e`, filled badge
  `#2e5277` with `#eaf3fb` icon, white info-chip `#ffffff` with `#2e5277` text,
  dark CTA pill `#0f1620`. — event / webinar / summit promo banners. Reads bright,
  corporate-event, energetic.

- **light mint / green + red-green gauges** (default for `graded-compare`): bg
  radial mint `#eef6ee`→`#e2f0e4`, panel `#ffffff`, line `#d6e4d8`, ink `#1d2a22`,
  muted `#5d6b62`, green accent `#3aa85a` (= the "good"/after color), red `#e8503a`
  (the "before" pill + low gauge), gauge tracks `#e3ebe4`, soft fills `#fdecea`
  (bad) / `#e9f7ec` (good), dark CTA `#16221b`. — before/after artifact-with-score
  posts (resume/profile/design "upgrade", audit before vs after). Reads clean,
  fresh, conversion-focused.

- **white poster / blue-panel + purple CTA** (default for `cheatsheet-wall`): bg
  white `#ffffff`, panel fill `#eef4fe`, panel line `#d4e2fb`, ink `#10131c`, muted
  `#41485c`, blue panel-header `#3567e6`, red title accent `#e8231f`, purple CTA band
  `#3b1d72` with a yellow highlight word `#ffd33a`, dark code block `#0e1830` /
  `#cfe0ff`, and three funnel-band tints `#f2c33d #ef7da0 #7db4ef`. — dense
  whole-topic "cheatsheet poster" references. Reads clean, energetic, save-worthy.

- **near-black cosmic / gradient-headline** (default for `partnership-banner`): bg
  radial `#0a1210`→`#050807`, panel `#0e1614`, line `#1c2b27`, ink `#ffffff`, muted
  `#8fa39c`, caps `#7f938c`, headline gradient mint `#8ff0b0`→cyan `#5fd0e0`→blue
  `#5aa6f0`, orange accent `#e8823a` (one logo mark + the hero rim-light), stat/proof
  icons in the mint/orange/cyan trio. — partnership / merger / acquisition
  announcements. Reads premium, cinematic, corporate-newsworthy.

- **white / per-layer multi-accent + purple CTA** (default for `layered-loop-map`): bg
  white `#ffffff`, panel `#ffffff`, line `#dfe3f2`, ink `#191d3a`, muted `#5a6180`,
  title indigo `#4b45e0` / violet `#7a5cf0`, four per-layer band accents L1 `#4b45e0`
  (indigo), L2 `#2f9e57` (green), L3 `#3f78d8` (blue), L4 `#d8892a` (amber), VS panels
  `#4b45e0` / `#c9962f`, purple CTA band `#2b2470`. Flow dots inherit each band's
  accent. — layered process / "N deepening levels of X" explainers with directional
  flow. Reads clean, technical, energetic.

- **purple-lilac / mint** (default for `lead-magnet-promo`): bg radial gradient
  lilac `#9a8fe6`→`#7d6fd1`→`#6657c0`, ink `#ffffff`, muted `#e7e2f8`, title-muted
  `#5b4fb0`, icon-badge `#6b5cc4`, mint CTA accent `#36e0a0`; cover card white
  `#ffffff` with a `#5b4bc4` band. — lead-magnet / "download this" promo posts.
  Reads soft, premium-marketing, approachable.

Keep contrast ≥ 4.5:1 for body text. If you change `--bg`/`--ink`, eyeball
the muted text — bump `--muted` lighter on dark, darker on light.

---

## Type (font pairings, loaded via CDN — no download)

Templates link Google Fonts in `<head>` and load Iconify in `<script>`. When
the render machine is online these resolve automatically; nothing is committed
to the repo.

- **Display / heading:** `Space Grotesk` 700 (default), or `Poppins` 700 for a
  softer/business feel, or `Sora` 700 for a more neutral-modern feel.
- **Body:** `Inter` 400/600.
- **Mono (eyebrows, code, labels):** `JetBrains Mono` 500.
- **Script accent (rare, decorative only):** `Caveat` — use sparingly.

To change a font: edit the `fonts.googleapis.com/css2?family=...` URL and the
`font-family` in the palette/CSS. Pick weights you actually use to keep the
fetch small.

Offline render fallback: if the machine has no network, CDN fonts/icons won't
load and text falls back to system fonts. In that case download the WOFF2 files
and reference them with `@font-face local paths`, and swap Iconify for inline
SVG. Do this only when offline is a hard requirement — do not commit font
binaries into this repo by default (repo weight + gitignore rules).

---

## Tuning (per-archetype) — read the one you're using

Detailed per-archetype tuning notes (sizing by content length, `data-*` knobs,
column/band counts, layout gotchas, build fixes) live in one file each under
`tuning/<archetype>.md` next to this skill. They are NOT loaded here to keep this
file lean — read only the file for the archetype you picked.

**Before you fill a template, read `tuning/<archetype>.md`** for that archetype
if one exists. Archetypes with a tuning file:

- `partnership-banner`, `cheatsheet-wall`, `graded-compare`, `chart-compare`,
  `cover-hero`, `person-spotlight`, `event-banner`, `lead-magnet-promo`,
  `architecture-map`, `layered-loop-map`, `animated-flow-map`, `hub-and-spoke`,
  `hiring-banner`, `think-vs-reality`, `comparison-columns`, `versus-list`,
  `carousel-slide`, `whiteboard-sketch`.

Archetypes not listed (`stat-banner`, `before-after`, `role-pipeline`,
`layered-stack`, `cheatsheet-grid`, `maturity-scale`) need no per-content tuning —
fill the template's placeholders, pick a palette, and render.

---

## Render pipeline

Headless Chrome cannot write into the repo dir on this machine (access denied),
so render to `$TEMP` and move the file.

```bash
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
TMP="$TEMP/li_$(date +%s).png"
UDD="$TEMP/cr_udd_$$"   # Chrome needs a user-data-dir in new headless
SRC="skills/content/marketing/linkedin-post/templates/stat-banner.html"

# Build a correct file:// URI (MSYS pwd is /d/...; Chrome needs file:///D:/...)
URI=$(python -c "import pathlib; print(pathlib.Path('$SRC').resolve().as_uri())")

"$CHROME" --headless=new --disable-gpu --no-sandbox \
  --user-data-dir="$UDD" --force-device-scale-factor=2 \
  --window-size=1080,1350 --hide-scrollbars \
  --virtual-time-budget=4000 --screenshot="$TMP" "$URI"

mv "$TMP" assets/linkedin/out.png
```

- Use `--headless=new` (current Chrome) and pass `--user-data-dir`, or Chrome
  errors with "Missing headless user data directory".
- Build the `file://` URI with Python's `as_uri()` — a raw `file://$(pwd)/...`
  fails on this machine because MSYS `pwd` returns `/d/...`, not `D:/...`, and
  Chrome silently screenshots its own ERR_FILE_NOT_FOUND page (~41 KB PNG). A
  correct render is much larger; if the PNG looks tiny, the URI was wrong.
- `--force-device-scale-factor=2` → retina-sharp (output is 2× the window size).
- `--window-size` must match the template's `--w/--h` intent: `1080,1350`
  portrait or `1200,627` landscape. If you change one, change both.
- `--virtual-time-budget=4000` gives CDN fonts/icons time to load before capture.

---

## Copy rules (inherited from content-engine)

Deliver copy as a block under the image. Structure:

- **Hook (line 1):** the claim or a sharp question. No "I'm excited to share".
  It must stand alone in the truncated feed preview.
- **Body (2–5 short lines / paragraphs):** the substance. Specific, concrete.
- **Optional list:** mirror the graphic's points; don't restate it verbatim.
- **Soft CTA (1 line):** a genuine prompt, not "comment GUIDE for the link".

Hard rules:
- One claim per post. No hype words (revolutionary, game-changer, insane).
- No emoji bullets, no reply-bait, no fake-vulnerability hook.
- Match the graphic — the post text and the image make the *same* point.

---

## Scope limits (be honest, don't fake)

This environment renders HTML/CSS → PNG. It **cannot** generate:

- Photoreal hero photos, 3D renders, or AI-illustrated scenes.
- These need an image-generation model not available here.

For those requests: **don't pretend to render them.** Instead deliver a
prompt-recipe — a ready-to-paste prompt (subject, style, lighting, palette,
aspect ratio) the user can run in their image tool, plus the copy block. Say
plainly that the visual is a prompt, not a rendered asset.

Animated dot-flow connectors are possible as animated SVG, but export is static
PNG by default; a GIF/MP4 export is extra work — flag it, don't assume it.

---

## Build note

This skill ships bundled HTML templates. `build-dist.py` copies the sibling
`linkedin-post/` folder's non-`.md` files into the installed skill. After
editing any template, run `python build-dist.py` and reinstall.
