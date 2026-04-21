# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website for Crystal Widjaja (www.crissyw.com) — plain static HTML served by GitHub Pages. Custom domain managed via the CNAME file.

## Development Commands

```bash
# Local preview (no build step needed)
python3 -m http.server
# Available at http://localhost:8000
```

There are no dependencies, build steps, tests, or linters.

## Architecture

**Pure static HTML** — no framework, no build tool. Each page is a self-contained HTML file with the shared head/nav inlined.

**Pages:**
- `/index.html` — home page (landing with jQuery rotating tagline)
- `/about-crystal-widjaja/index.html` — about page
- `/reading-list/index.html` — curated book list (22 entries, all hardcoded in HTML)
- `/reading_list/index.html` — meta-refresh redirect to `/reading-list`
- `/404.html` — custom GitHub Pages 404

**Static assets** live under `static/` (CSS, JS, images). All pages reference assets with absolute paths (`/static/...`).

**CDN dependencies:** Bootstrap 4.1, jQuery 3.4.1, Google Fonts (Lato, Catamaran, Roboto Condensed).

**Analytics:** Google Tag Manager, Google Analytics (UA), Twitter pixel — all in the `<head>` of each page.
