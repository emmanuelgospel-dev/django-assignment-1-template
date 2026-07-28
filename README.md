# Akax Portfolio

A Django portfolio site — Homepage, Skills, Blog (full CRUD), and Contact.

## Stack
- Django 6.0 (works fine on Django 5.x too — see `requirements.txt`)
- SQLite (default dev database)
- Vanilla JS + hand-rolled CSS (no frontend framework)
- Google Fonts: Inter, Playfair Display, IBM Plex Mono

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations (already applied in this handoff, but harmless to re-run)
python manage.py migrate

# 4. Create your own superuser (a demo one already exists — see below)
python manage.py createsuperuser

# 5. (Optional) Seed sample skills + blog posts
python manage.py seed_data

# 6. Run the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Demo admin login (already seeded in db.sqlite3)
- Username: `akax`
- Password: `akaxadmin123`

**Change this password or delete the user before deploying anywhere public.**

## Pages
| URL | Page | Auth |
|-----|------|------|
| `/` | Homepage — hero, featured skills, latest posts | Public |
| `/skills/` | Skills & tools, grouped, with progress bars | Public |
| `/blog/` | Blog list with category tab filtering (no reload) | Public |
| `/blog/new/` | Create post | Login required |
| `/blog/<slug>/` | Post detail (Edit/Delete buttons show if logged in) | Public to view |
| `/blog/<slug>/edit/` | Edit post | Login required |
| `/blog/<slug>/delete/` | Delete confirmation | Login required |
| `/contact/` | Contact form → saves to DB | Public |
| `/login/`, `/logout/` | Admin auth | Public |
| `/admin/` | Django admin — manage all content | Superuser |

## Adding skills / managing content
Go to `/admin/`, log in, and add `Skill` entries. Category choices: Backend, Frontend,
Design, Tools. Toggle `is_tool` to split an entry into the "Tools" section on the Skills
page. `order` controls sort position (lower = first).



## Design system
Near-black background (`#0a0a0b`) with a warm gold accent (`#d4a857`), glassmorphism
cards (`backdrop-filter: blur`), Playfair Display for headings, Inter for body text,
IBM Plex Mono for eyebrow labels and category tags. Tokens live in
`static/css/base.css` as CSS custom properties — full dark/light theme swap via
`data-theme` attribute + `localStorage`.

Dark/light theme toggle, mobile hamburger nav, scroll-reveal animations, and blog
category tab filtering (JS, no page reload) **are** implemented.

## Known gaps to fix before deploying to production
- `SECRET_KEY` is hardcoded in `settings.py` — move to environment variable
- `DEBUG = True` — set to `False` and configure `ALLOWED_HOSTS` for your real domain
- No automated tests yet
