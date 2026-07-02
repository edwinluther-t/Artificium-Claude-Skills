---
name: design
description: Unified design skill covering brand identity, design tokens, UI styling, logo design, corporate identity programs, HTML presentations, banner design, icon design, and social media images. Use when designing logos, brand systems, banners, slides, icons, or social media visuals.
---

# Design

Unified design skill: brand, tokens, UI, logo, CIP, slides, banners, social photos, icons.

## When to Use

- Brand identity, voice, assets
- Design system tokens and specs
- UI styling with shadcn/ui + Tailwind
- Logo design
- Corporate identity program (CIP) deliverables
- Presentations and pitch decks
- Banner design for social media, ads, web, print
- Social photos for Instagram, Facebook, LinkedIn, Twitter, Pinterest, TikTok

## Sub-skill Routing

| Task | Sub-skill | Details |
|------|-----------|---------|
| Brand identity, voice, assets | `brand` | External skill |
| Tokens, specs, CSS vars | `design-system` | External skill |
| shadcn/ui, Tailwind, code | `ui-styling` | External skill |
| Logo creation | Logo (built-in) | `references/logo-design.md` |
| CIP mockups, deliverables | CIP (built-in) | `references/cip-design.md` |
| Presentations, pitch decks | Slides (built-in) | `references/slides.md` |
| Banners, covers, headers | Banner (built-in) | `references/banner-sizes-and-styles.md` |
| Social media images/photos | Social Photos (built-in) | `references/social-photos-design.md` |
| SVG icons, icon sets | Icon (built-in) | `references/icon-design.md` |

## Logo Design (Built-in)

55+ styles, 30 color palettes, 25 industry guides.

### Logo: Generate Design Brief

```bash
python3 ~/.claude/skills/design/scripts/logo/search.py "tech startup modern" --design-brief -p "BrandName"
```

### Logo: Search Styles/Colors/Industries

```bash
python3 ~/.claude/skills/design/scripts/logo/search.py "minimalist clean" --domain style
python3 ~/.claude/skills/design/scripts/logo/search.py "tech professional" --domain color
python3 ~/.claude/skills/design/scripts/logo/search.py "healthcare medical" --domain industry
```

### Logo: Generation

**ALWAYS** generate output logo images with white background.

```bash
python3 ~/.claude/skills/design/scripts/logo/generate.py --brand "TechFlow" --style minimalist --industry tech
python3 ~/.claude/skills/design/scripts/logo/generate.py --prompt "coffee shop vintage badge" --style vintage
```

**IMPORTANT:** When scripts fail, try to fix them directly.

After generation, **ALWAYS** ask user about HTML preview via `AskUserQuestion`. If yes, invoke `/ui-ux-pro-max` for gallery.

## CIP Design (Built-in)

50+ deliverables, 20 styles, 20 industries.

### CIP: Generate Brief

```bash
python3 ~/.claude/skills/design/scripts/cip/search.py "tech startup" --cip-brief -b "BrandName"
```

### CIP: Search Domains

```bash
python3 ~/.claude/skills/design/scripts/cip/search.py "business card letterhead" --domain deliverable
python3 ~/.claude/skills/design/scripts/cip/search.py "luxury premium elegant" --domain style
python3 ~/.claude/skills/design/scripts/cip/search.py "hospitality hotel" --domain industry
python3 ~/.claude/skills/design/scripts/cip/search.py "office reception" --domain mockup
```

### CIP: Generate Mockups

```bash
# With logo (RECOMMENDED)
python3 ~/.claude/skills/design/scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card" --industry "consulting"

# Full CIP set
python3 ~/.claude/skills/design/scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --industry "consulting" --set

# Without logo
python3 ~/.claude/skills/design/scripts/cip/generate.py --brand "TechFlow" --deliverable "business card" --no-logo-prompt
```

### CIP: Render HTML Presentation

```bash
python3 ~/.claude/skills/design/scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images /path/to/cip-output
```

**Tip:** If no logo exists, use Logo Design section above first.

## Slides (Built-in)

Strategic HTML presentations with Chart.js, design tokens, copywriting formulas.

Load `references/slides-create.md` for the creation workflow.

### Slides: Knowledge Base

| Topic | File |
|-------|------|
| Creation Guide | `references/slides-create.md` |
| Layout Patterns | `references/slides-layout-patterns.md` |
| HTML Template | `references/slides-html-template.md` |
| Copywriting | `references/slides-copywriting-formulas.md` |
| Strategies | `references/slides-strategies.md` |

## Banner Design (Built-in)

22 art direction styles across social, ads, web, print.

Load `references/banner-sizes-and-styles.md` for complete sizes and styles reference.

### Banner: Workflow

1. **Gather requirements** via `AskUserQuestion` — purpose, platform, content, brand, style, quantity
2. **Research** — distill references into layout anatomy + a sampled 5–6 hex palette + a mood-matched font pairing + an icon style (see Rendering discipline below)
3. **Design** — Create HTML/CSS banner; palette as `:root` vars, `.wrap{flex-direction:column}` with the main region `flex:1`
4. **Export** — Render to PNG via headless Chrome at exact dimensions (see Rendering discipline). Build the `file://` URI with Python `as_uri()`; render at 2× for retina
5. **Verify** — open the exported PNG and look at it; fix dead space / overflow / ragged heights and re-render
6. **Present** — Show all options side-by-side, iterate on feedback

### Banner: Quick Size Reference

| Platform | Type | Size (px) |
|----------|------|-----------|
| Facebook | Cover | 820 x 312 |
| Twitter/X | Header | 1500 x 500 |
| LinkedIn | Personal | 1584 x 396 |
| YouTube | Channel art | 2560 x 1440 |
| Instagram | Story | 1080 x 1920 |
| Instagram | Post | 1080 x 1080 |
| Google Ads | Med Rectangle | 300 x 250 |
| Website | Hero | 1920 x 600-1080 |

### Banner: Top Art Styles

| Style | Best For |
|-------|----------|
| Minimalist | SaaS, tech |
| Bold Typography | Announcements |
| Gradient | Modern brands |
| Photo-Based | Lifestyle, e-com |
| Geometric | Tech, fintech |
| Glassmorphism | SaaS, apps |
| Neon/Cyberpunk | Gaming, events |

### Banner: Design Rules

- Safe zones: critical content in central 70-80%
- One CTA per banner, bottom-right, min 44px height
- Max 2 fonts, min 16px body, ≥32px headline
- Text under 20% for ads (Meta penalizes)
- Print: 300 DPI, CMYK, 3-5mm bleed

## Icon Design (Built-in)

Icons come from the Iconify CDN — thousands of open-source icons across many sets,
no generation model or bundled binaries needed. Load Iconify once and reference an
icon by `set:name`.

### Icon: Use in HTML/CSS

```html
<script src="https://code.iconify.design/3/3.1.1/iconify.min.js"></script>
<!-- then, anywhere: -->
<span class="iconify" data-icon="lucide:settings" style="color:#6366F1"></span>
<span class="iconify" data-icon="lucide:shopping-cart"></span>
```

- **Match the icon set's STYLE to the medium**, not just the meaning: clean
  flat-line UI → `lucide` / `iconoir`; hand-drawn/marker/sketchnote →
  `streamline-freehand` (wobbly pen stroke); duotone marketing → `lucide` two-tone
  or a duotone set. Color icons with a CSS var so a retheme is one edit.
- **Verify names before you use them** — a wrong name renders as a silent blank
  gap (no error). Confirm every chosen name resolves in one batch call:
  `curl -s "https://api.iconify.design/lucide.json?icons=settings,cart,user"` →
  JSON with `not_found: []` means all exist. Some sets have verbose/inconsistent
  names (e.g. `streamline-freehand`), so never guess — validate.
- Need standalone SVG files (for a native app, favicon, multi-size export)?
  Fetch from the API: `curl "https://api.iconify.design/lucide/settings.svg"`,
  or add `?width=48&color=%236366F1` for size/color.

### Icon: Top Styles

| Style | Best For |
|-------|----------|
| outlined | UI interfaces, web apps |
| filled | Mobile apps, nav bars |
| duotone | Marketing, landing pages |
| rounded | Friendly apps, health |
| sharp | Tech, fintech, enterprise |
| flat | Material design, Google-style |
| gradient | Modern brands, SaaS |

## Social Photos (Built-in)

Multi-platform social image design: HTML/CSS → screenshot export.

Load `references/social-photos-design.md` for sizes, templates, best practices.

### Social Photos: Workflow

1. **Orchestrate** — parallel subagents for independent work
2. **Analyze** — Parse prompt: subject, platforms, style, brand context, content elements
3. **Ideate** — 3-5 concepts, present via `AskUserQuestion`
4. **Design** — brand → design-system → ui-ux-pro-max; HTML per idea × size; palette as `:root` vars, mood-matched fonts, CDN icons
5. **Export** — Render to PNG via headless Chrome at exact px, 2× device-scale (see Rendering discipline). Build the `file://` URI with Python `as_uri()`
6. **Verify** — open every exported PNG and look at it; fix layout/styling issues and re-export
7. **Report** — Summary to `plans/reports/` with design decisions
8. **Organize** — Sort output files and reports

For LinkedIn/social-post INFOGRAPHICS specifically (ready archetype templates +
copy discipline), the `linkedin-post` skill has 24 self-contained HTML templates
and a proven pipeline — prefer it over hand-building a feed infographic here.

### Social Photos: Key Sizes

| Platform | Size (px) | Platform | Size (px) |
|----------|-----------|----------|-----------|
| IG Post | 1080×1080 | FB Post | 1200×630 |
| IG Story | 1080×1920 | X Post | 1200×675 |
| IG Carousel | 1080×1350 | LinkedIn | 1200×627 |
| YT Thumb | 1280×720 | Pinterest | 1000×1500 |

## Rendering discipline (HTML/CSS → PNG)

Any static visual this skill produces — banner, social image, slide, dashboard
mockup, logo lockup — is HTML/CSS rendered to PNG with headless Chrome. This is
the whole pipeline; there is no image-generation model assumed.

**Render pipeline:**

```bash
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"  # adjust per OS
TMP="$TEMP/render_$(date +%s).png"; UDD="$TEMP/cr_udd_$$"
SRC="path/to/design.html"
# file://$(pwd) can silently screenshot Chrome's error page (tell: a tiny ~40KB
# PNG). Build the URI with Python as_uri() instead:
URI=$(python -c "import pathlib; print(pathlib.Path('$SRC').resolve().as_uri())")
"$CHROME" --headless=new --disable-gpu --no-sandbox --user-data-dir="$UDD" \
  --force-device-scale-factor=2 --window-size=1080,1350 --hide-scrollbars \
  --virtual-time-budget=4000 --screenshot="$TMP" "$URI"
mv "$TMP" assets/out.png
```

- `--headless=new` + `--user-data-dir` required; `--force-device-scale-factor=2`
  for retina (output is 2× the window). `--window-size` MUST match the design's
  `--w/--h`. `--virtual-time-budget` lets CDN fonts/icons load first.
- **Always open the PNG and look at it before presenting.** Correct render = 100s
  of KB at 2×; a tiny PNG means the URI was wrong. Fix dead space / overflow /
  ragged heights and re-render.

**Theming — palette as CSS vars:** put a 5–6 var block FIRST at `:root`
(`--bg --panel --line --ink --muted --accent` + any per-item accents). Reference
the vars everywhere so a full retheme (or light/dark swap) is a few-line edit.
Sample real hex from the reference/brand; don't force one house palette. Keep body
contrast ≥ 4.5:1.

**Type by mood:** dev/tech → Space Grotesk / JetBrains Mono; bright/editorial →
Poppins; soft/rounded → Baloo 2; body almost always Inter. Match the closest
open-source Google Font; never claim a proprietary one.

**Un-renderable art (honest scope):** photoreal/3D/AI illustrations can't be
generated here. Build the structure in CSS, expose an IMAGE SLOT
(`background-image`) for user-supplied art, and hand over a prompt-recipe. Never
fake generated art.

**Hybrid composition:** a design can borrow a self-contained block from another
layout (a stat hero, a CTA band, an icon-list rail). Keep ONE base that owns the
canvas + palette + footer; graft 1–2 blocks and restyle them to the base vars.
Don't fuse two bases (two canvases/palettes) into one image.

## Dashboard & app-chrome layouts (same discipline)

The render + theming + icon discipline above applies directly to app UI — a
dashboard, admin panel, or product screen is just a bigger HTML/CSS surface. Build
it from composable REGIONS, each themed by the same `:root` vars:

- **Top bar** — brand mark left, page title/search center, user/actions right;
  fixed height (`56–64px`), `--panel` bg, `--line` bottom border.
- **Left nav** — a fixed-width rail (`220–260px`, or a `64px` icon-only rail);
  CDN icons (verify names) + labels; active item uses `--accent`; collapsible.
- **Content region** — `flex:1` so it fills between top bar and footer; grid of
  cards/panels, each a themed block (stat card, chart panel, table, list).
- **Footer** — thin `--muted` status/meta row, or omit.
- **Layout shell:** `body{display:flex}` → left nav + a right
  `flex:1;flex-direction:column` column holding top bar → `main{flex:1}` →
  footer. Give the scrolling content region `overflow:auto`.
- **Light/dark:** because color lives in `:root` vars, a dark theme is a second
  var set toggled on `<body data-theme="dark">` — don't hardcode colors in
  components. Chart colors, borders, and icon tints all read from vars.
- Cards/panels borrow the same block patterns as posters (stat numeral, list
  rail, progress/chevron row) — reuse them, restyled to the app palette.

## Workflows

### Complete Brand Package

1. **Logo** → `scripts/logo/generate.py` → Generate logo variants
2. **CIP** → `scripts/cip/generate.py --logo ...` → Create deliverable mockups
3. **Presentation** → Load `references/slides-create.md` → Build pitch deck

### New Design System

1. **Brand** (brand skill) → Define colors, typography, voice
2. **Tokens** (design-system skill) → Create semantic token layers
3. **Implement** (ui-styling skill) → Configure Tailwind, shadcn/ui

## References

| Topic | File |
|-------|------|
| Design Routing | `references/design-routing.md` |
| Logo Design Guide | `references/logo-design.md` |
| Logo Styles | `references/logo-style-guide.md` |
| Logo Colors | `references/logo-color-psychology.md` |
| Logo Prompts | `references/logo-prompt-engineering.md` |
| CIP Design Guide | `references/cip-design.md` |
| CIP Deliverables | `references/cip-deliverable-guide.md` |
| CIP Styles | `references/cip-style-guide.md` |
| CIP Prompts | `references/cip-prompt-engineering.md` |
| Slides Create | `references/slides-create.md` |
| Slides Layouts | `references/slides-layout-patterns.md` |
| Slides Template | `references/slides-html-template.md` |
| Slides Copy | `references/slides-copywriting-formulas.md` |
| Slides Strategy | `references/slides-strategies.md` |
| Banner Sizes & Styles | `references/banner-sizes-and-styles.md` |
| Social Photos Guide | `references/social-photos-design.md` |
| Icon Design Guide | `references/icon-design.md` |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/logo/search.py` | Search logo styles, colors, industries |
| `scripts/logo/generate.py` | Generate logos |
| `scripts/logo/core.py` | BM25 search engine for logo data |
| `scripts/cip/search.py` | Search CIP deliverables, styles, industries |
| `scripts/cip/generate.py` | Generate CIP mockups |
| `scripts/cip/render-html.py` | Render HTML presentation from CIP mockups |
| `scripts/cip/core.py` | BM25 search engine for CIP data |

Icons do NOT use a script — they load from the Iconify CDN (see Icon Design
above). Fetch standalone SVGs from the API when needed
(`curl "https://api.iconify.design/lucide/settings.svg"`).

## Prerequisites

**Python:** This skill uses Python scripts. On Windows, use `python` instead of `python3` (e.g., `python scripts/logo/search.py` instead of `python3 scripts/logo/search.py`).

Check if Python is installed:
```bash
python3 --version || python --version
```

## Integration

**External sub-skills:** brand, design-system, ui-styling
**Related Skills:** frontend-design, ui-ux-pro-max
