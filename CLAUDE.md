# CLAUDE.md - AI Assistant Guide for Crystal Widjaja's Website

## Project Overview

This is Crystal Widjaja's personal portfolio website, a Flask-based web application hosted at **www.crissyw.com**. The site showcases her professional background, reading recommendations, and links to her various projects including Generation Girl (non-profit).

## Technology Stack

- **Backend**: Python 3.8+ with Flask 3.0.3
- **Templating**: Jinja2
- **Frontend**: HTML5, CSS3, JavaScript (jQuery 3.4.1)
- **CSS Framework**: Bootstrap 4.1.0
- **Production Server**: Gunicorn 22.0.0
- **Deployment**: Heroku (via Procfile)
- **Analytics**: Google Analytics, Google Tag Manager, Twitter Pixel

## Directory Structure

```
website/
├── app.py              # Main Flask application with routes
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
├── CNAME              # Custom domain configuration (www.crissyw.com)
├── .gitignore         # Git ignore rules
├── README.md          # Basic project documentation
├── templates/         # Jinja2 HTML templates
│   ├── base.html      # Base template with nav, head, analytics
│   ├── home.html      # Homepage with animated text
│   ├── about-crystal-widjaja.html  # About page
│   ├── reading-list.html           # Reading recommendations
│   └── index.html     # Test/alternate template
└── static/            # Static assets
    ├── css/
    │   ├── base.css   # Global styles (nav, body)
    │   ├── home.css   # Homepage-specific styles
    │   └── work.css   # Additional styles
    ├── js/
    │   └── home.js    # jQuery animations and hash routing
    ├── images/
    │   ├── portfolio/     # Portfolio images
    │   ├── reading-list/  # Book cover images
    │   └── [social icons] # Social media icons
    └── sitemap.xml    # SEO sitemap
```

## Application Routes

| Route | Function | Template |
|-------|----------|----------|
| `/` | `index()` | home.html |
| `/about-crystal-widjaja` | `about()` | about-crystal-widjaja.html |
| `/reading-list` | `readingList()` | reading-list.html |
| `/reading_list` | Redirects to `/reading-list` | - |
| `/actualtest` | `actualtest()` | index.html |

## Key Conventions

### Template Structure
- All page templates extend `base.html`
- Use `{% block head %}` for page-specific CSS/JS includes
- Use `{% block body %}` for main content
- Bootstrap 4 and jQuery are loaded per-page in child templates

### CSS Organization
- `base.css`: Global styles (navigation, body defaults)
- `home.css`: Homepage-specific styles (banner, icons)
- Uses Catamaran and Lato Google Fonts

### Static File References
- Use Flask's `url_for()` for CSS/JS: `{{ url_for('static', filename='css/home.css') }}`
- Images can use relative paths in templates: `static/images/...`

### Data Patterns
- Reading list data is defined as dictionaries in `app.py` (lines 25-60)
- Each book entry contains: `url`, `file_path`, `book_summary`
- Data is passed to templates via `render_template()`

### Analytics Integration
- Google Tag Manager ID: `GTM-N9XPWJV`
- Google Analytics ID: `UA-167313514-1`
- Twitter Pixel ID: `o49c2`
- Outbound link tracking via `getOutboundLink()` function

## Development Workflow

### Local Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
flask run
# or
python app.py
```

The app runs at `http://127.0.0.1:5000` with debug mode enabled.

### Configuration Notes
- Static file caching is disabled in development: `SEND_FILE_MAX_AGE_DEFAULT = 0`
- Debug mode is enabled when running via `python app.py`

### Production Deployment
Deployed via Heroku with Gunicorn:
```
web: gunicorn --bind 0.0.0.0:$PORT app:app
```

## Guidelines for AI Assistants

### When Modifying Templates
1. Always extend `base.html` for new pages
2. Include Bootstrap and jQuery in `{% block head %}` if using Bootstrap components
3. Maintain consistent navigation by not modifying `base.html` nav without explicit request
4. Use Bootstrap 4 grid system for layouts

### When Adding New Routes
1. Add route handler in `app.py`
2. Create corresponding template in `templates/`
3. Follow existing naming conventions (lowercase, hyphen-separated)
4. Add SEO redirects for alternate URL patterns if needed

### When Adding Reading List Items
Books are organized in categories in `app.py`:
- `management` - Leadership books
- `enduring_company` - Business strategy
- `user_empathy` - Customer communication
- `data_literate` - Data/analytics
- `code_literate` - Technical resources

Format for new entries:
```python
'Book Title — Author': {
    'url': 'https://...',
    'file_path': 'static/images/reading-list/filename.jpg',
    'book_summary': 'Summary text...'
}
```

### When Modifying Styles
- Global changes go in `base.css`
- Page-specific styles go in corresponding CSS files
- Follow existing naming patterns (lowercase, BEM-like)

### Important Files to Preserve
- `CNAME` - Critical for custom domain
- `Procfile` - Required for Heroku deployment
- Analytics scripts in `base.html` - Business-critical tracking

### Testing Changes
1. Run `flask run` to start local server
2. Test all routes: `/`, `/about-crystal-widjaja`, `/reading-list`
3. Verify responsive design at various viewport sizes
4. Check that animations work (text rotation on homepage)

## Dependencies

From `requirements.txt`:
- click==8.1.7
- Flask==3.0.3
- gunicorn==22.0.0
- itsdangerous==2.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- Werkzeug==3.0.3
