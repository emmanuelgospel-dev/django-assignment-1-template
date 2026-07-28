# Akax Portfolio

A Django portfolio site — Homepage, Skills, Blog (full CRUD), and Contact.

## Stack
- Django 6.0 (works fine on Django 5.x too — see `requirements.txt`)
- SQLite (default dev database)
- Vanilla JS + hand-rolled CSS (no frontend framework)
- Google Fonts: Inter, Playfair Display, IBM Plex Mono

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

## Design system
Near-black background (`#0a0a0b`) with a warm gold accent (`#d4a857`), glassmorphism
cards (`backdrop-filter: blur`), Playfair Display for headings, Inter for body text,
IBM Plex Mono for eyebrow labels and category tags. Tokens live in
`static/css/base.css` as CSS custom properties — full dark/light theme swap via
`data-theme` attribute + `localStorage`.

Dark/light theme toggle, mobile hamburger nav, scroll-reveal animations, and blog
category tab filtering (JS, no page reload) **are** implemented.
