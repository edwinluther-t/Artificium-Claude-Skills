---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
---

# Web Artifacts Builder

To build powerful frontend artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

**Theme with CSS variables, never hardcoded color.** shadcn/ui already exposes
its palette as HSL vars (`--background --foreground --card --border --primary
--muted-foreground`) — drive every component off those, so a full retheme or a
light/dark swap is editing one `:root` / `.dark` block, not the components. Sample
a real palette (from the brand or a reference) into those vars rather than shipping
the shadcn default slate; pick a genuine accent, not generic indigo.

**App-shell / dashboard layout — compose from regions.** A dashboard or app screen
is a shell of themed regions: a top bar (`h-14/16`, brand + title + actions), a
left nav rail (`w-56/64`, or a `w-16` icon rail; active item uses `--primary`), a
`flex-1 overflow-auto` content region (a grid of cards/panels), an optional thin
footer. Shell = `flex` row: nav + a `flex-1 flex-col` column holding the top bar →
`main flex-1` → footer. Each card is a themed block; reuse a card's shape across
the grid.

**Inline data-viz: prefer real CSS/SVG charts** (or a lib like Recharts) over an
image. A pie is a `conic-gradient`; a bar/spark row is flex'd divs; color the
series from theme vars so charts retheme with the app. Only reach for a raster
image when the visual genuinely can't be built in the DOM.

**Icons from a CDN set — and verify names.** Use `lucide-react` (already in the
stack) or Iconify for anything else. Match the set's stroke to the medium. If you
reference an icon by string name (Iconify), confirm it resolves first
(`curl -s "https://api.iconify.design/lucide.json?icons=a,b,c"` → `not_found: []`)
— a wrong name renders as a silent blank gap.

**Verify the rendered output before presenting.** After bundling, actually view
the artifact (Step 5) at least once for anything non-trivial — look at it, fix
overflow / dead space / ragged card heights, don't ship a layout you haven't seen.

**Honest scope on art.** Photoreal photos, 3D renders, and AI illustrations can't
be generated here. Build the structure and leave a real image slot (an `<img>` /
`background-image` the user fills) plus a ready-to-paste prompt-recipe — never fake
a generated asset.

**Compose, don't clone (hybrid).** A screen can borrow a self-contained block from
another layout — a stat-hero, a proof-stat strip, a CTA band, an icon-list rail.
Keep ONE base that owns the canvas + palette + shell; graft one or two blocks and
restyle them to the theme vars. Don't fuse two different palettes/shells into one
screen.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- React + TypeScript (via Vite)
- Tailwind CSS 3.4.1 with shadcn/ui theming system
- Path aliases (`@/`) configured
- 40+ shadcn/ui components pre-installed
- All Radix UI dependencies included
- Parcel configured for bundling (via .parcelrc)
- Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components
