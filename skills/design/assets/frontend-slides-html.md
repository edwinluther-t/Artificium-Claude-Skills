---
name: frontend-slides
description: Create zero-dependency, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch. Helps users discover their aesthetic through visual exploration rather than abstract choices.
---

# Frontend Slides

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

## When to Activate

- Creating a talk deck, pitch deck, workshop deck, or internal presentation
- Converting `.ppt` or `.pptx` slides into an HTML presentation
- Improving an existing HTML presentation's layout, motion, or typography
- Exploring presentation styles with a user who does not know their design preference yet

## Non-Negotiables

1. **Zero dependencies**: default to one self-contained HTML file with inline CSS and JS.
2. **Viewport fit is mandatory**: every slide must fit inside one viewport with no internal scrolling.
3. **Show, don't tell**: use visual previews instead of abstract style questionnaires.
4. **Distinctive design**: avoid generic purple-gradient, Inter-on-white, template-looking decks.
5. **Production quality**: keep code commented, accessible, responsive, and performant.

Before generating, read `STYLE_PRESETS.md` for the viewport-safe CSS base, density limits, preset catalog, and CSS gotchas.

## Workflow

### 1. Detect Mode

Choose one path:
- **New presentation**: user has a topic, notes, or full draft
- **PPT conversion**: user has `.ppt` or `.pptx`
- **Enhancement**: user already has HTML slides and wants improvements

### 2. Discover Content

Ask only the minimum needed:
- purpose: pitch, teaching, conference talk, internal update
- length: short (5-10), medium (10-20), long (20+)
- content state: finished copy, rough notes, topic only

If the user has content, ask them to paste it before styling.

### 3. Discover Style

Default to visual exploration.

If the user already knows the desired preset, skip previews and use it directly.

Otherwise:
1. Ask what feeling the deck should create: impressed, energized, focused, inspired.
2. Generate **3 single-slide preview files** in a design previews folder.
3. Each preview must be self-contained, show typography/color/motion clearly, and stay under roughly 100 lines of slide content.
4. Ask the user which preview to keep or what elements to mix.

Use the preset guide in `STYLE_PRESETS.md` when mapping mood to style.

### 4. Build the Presentation

Output either:
- `presentation.html`
- `[presentation-name].html`

Use an `assets/` folder only when the deck contains extracted or user-supplied images.

Required structure:
- semantic slide sections
- a viewport-safe CSS base from `STYLE_PRESETS.md`
- CSS custom properties for theme values
- a presentation controller class for keyboard, wheel, and touch navigation
- Intersection Observer for reveal animations
- reduced-motion support

### 5. Enforce Viewport Fit

Treat this as a hard gate.

Rules:
- every `.slide` must use `height: 100vh; height: 100dvh; overflow: hidden;`
- all type and spacing must scale with `clamp()`
- when content does not fit, split into multiple slides
- never solve overflow by shrinking text below readable sizes
- never allow scrollbars inside a slide

Use the density limits and mandatory CSS block in `STYLE_PRESETS.md`.

### 6. Validate

Check the finished deck at these sizes:
- 1920x1080
- 1280x720
- 768x1024
- 375x667
- 667x375

If browser automation is available, use it to verify no slide overflows and that keyboard navigation works.

### 7. Deliver

At handoff:
- delete temporary preview files unless the user wants to keep them
- open the deck with the platform-appropriate opener when useful
- summarize file path, preset used, slide count, and easy theme customization points

Use the correct opener for the current OS:
- macOS: `open file.html`
- Linux: `xdg-open file.html`
- Windows: `start "" file.html`

## PPT / PPTX Conversion

For PowerPoint conversion:
1. Prefer `python3` with `python-pptx` to extract text, images, and notes.
2. If `python-pptx` is unavailable, ask whether to install it or fall back to a manual/export-based workflow.
3. Preserve slide order, speaker notes, and extracted assets.
4. After extraction, run the same style-selection workflow as a new presentation.

Keep conversion cross-platform. Do not rely on macOS-only tools when Python can do the job.

## Implementation Requirements

### HTML / CSS

- Use inline CSS and JS unless the user explicitly wants a multi-file project.
- Fonts may come from Google Fonts or Fontshare.
- Prefer atmospheric backgrounds, strong type hierarchy, and a clear visual direction.
- Use abstract shapes, gradients, grids, noise, and geometry rather than illustrations.
- **Theme with CSS variables at `:root`** — a 5–6 var palette
  (`--bg --panel --line --ink --muted --accent`) referenced by every slide, so the
  whole deck rethemes (or gets a light/dark variant) from one block. Sample real hex
  from the topic/brand; don't scatter hardcoded color across slides.
- **Type by mood:** dev/tech → Space Grotesk / JetBrains Mono; bright/editorial →
  Poppins; body Inter. Match the closest open-source font; never claim a proprietary
  one.
- **Icons via Iconify CDN, matched to the medium and VERIFIED.** Flat deck → `lucide`;
  hand-drawn → `streamline-freehand`. Confirm names resolve before use
  (`curl -s "https://api.iconify.design/lucide.json?icons=a,b"` → `not_found: []`) —
  a wrong name is a silent blank gap.
- **Inline data-viz as real CSS/SVG**, not screenshots: a `conic-gradient` pie, a
  flex'd bar/spark row, a conic-ring gauge — colored from the theme vars so charts
  match the deck and stay crisp.
- **Hybrid slide composition:** a slide can borrow a self-contained block from another
  layout (a giant stat numeral, a comparison-columns block, a chevron progression, a
  quote band). Keep the deck's ONE base theme; graft the block and restyle it to the
  palette vars — don't introduce a second palette per slide.

### Rendering / export & honest scope

- If exporting slides to images with headless Chrome, build the `file://` URI with
  Python `pathlib.as_uri()` — a raw `file://$(pwd)` can silently screenshot Chrome's
  error page (tell: a tiny output file). Render at `--force-device-scale-factor=2`
  with a `--window-size` matching the slide canvas, and **open the export and look at
  it** before delivering.
- **No image-generation model is assumed here** — photoreal photos, 3D renders, and
  AI illustrations can't be produced. Build the structure in CSS and leave a real
  image slot for user-supplied art plus a ready-to-paste prompt-recipe. Never fake a
  generated visual (this is why abstract CSS shapes/gradients are preferred over
  illustrations above).

### JavaScript

Include:
- keyboard navigation
- touch / swipe navigation
- mouse wheel navigation
- progress indicator or slide index
- reveal-on-enter animation triggers

### Accessibility

- use semantic structure (`main`, `section`, `nav`)
- keep contrast readable
- support keyboard-only navigation
- respect `prefers-reduced-motion`

## Content Density Limits

Use these maxima unless the user explicitly asks for denser slides and readability still holds:

| Slide type | Limit |
|------------|-------|
| Title | 1 heading + 1 subtitle + optional tagline |
| Content | 1 heading + 4-6 bullets or 2 short paragraphs |
| Feature grid | 6 cards max |
| Code | 8-10 lines max |
| Quote | 1 quote + attribution |
| Image | 1 image constrained by viewport |

## Anti-Patterns

- generic startup gradients with no visual identity
- system-font decks unless intentionally editorial
- long bullet walls
- code blocks that need scrolling
- fixed-height content boxes that break on short screens
- invalid negated CSS functions like `-clamp(...)`

## Deliverable Checklist

- presentation runs from a local file in a browser
- every slide fits the viewport without scrolling
- style is distinctive and intentional
- animation is meaningful, not noisy
- reduced motion is respected
- file paths and customization points are explained at handoff
