# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website for Crystal Widjaja (www.crissyw.com) — a Flask app serving static pages. Deployed via Heroku (Procfile with gunicorn). Domain managed through a CNAME file for GitHub Pages / custom domain.

## Development Commands

```bash
# Setup
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run dev server (with debug mode)
python app.py
# Or:
flask run
# Available at http://127.0.0.1:5000

# Production (what Heroku runs)
gunicorn --bind 0.0.0.0:$PORT app:app
```

There are no tests, linters, or build steps configured.

## Architecture

**Backend:** Single Flask app (`app.py`) with four routes:
- `/` → `home.html` (landing page with rotating tagline animation)
- `/about-crystal-widjaja` → about page
- `/reading-list` → curated book list (data is defined inline in `app.py` as Python dicts, not in a database)
- `/reading_list` → redirect to `/reading-list`

**Templating:** Jinja2 templates in `templates/` extend `base.html`, which provides the nav bar, Google Analytics/GTM tracking, and OpenGraph meta tags. Each page template pulls in its own CSS/JS and Bootstrap 4.1 via CDN.

**Static assets:** `static/css/` for stylesheets, `static/js/home.js` for the jQuery-based tagline rotation on the home page, `static/images/` for logos and book cover images.

**Key detail:** Static asset caching is disabled (`SEND_FILE_MAX_AGE_DEFAULT = 0`) to force hard refreshes during development.
