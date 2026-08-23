# Adabala Satya Sai — Portfolio (Django)

A dark, glassmorphism-style developer portfolio built with Django. It presents
one dual identity — **Software Engineer** and **Data Analyst** — through a
live mode switch in the navbar (top right: **SE / DA**) that recolors the
page and swaps copy, resume download, and which projects/skills/experience
are emphasized.

Everything shown on the page (projects, skills, experience, education,
certifications, resume files, contact info) is stored in the database and
editable from Django Admin — no HTML editing required after setup.

---

## 1. Tech Stack

Python · Django 6 · SQLite (dev) / PostgreSQL-ready (prod) · vanilla
HTML/CSS/JS · WhiteNoise for static files · Google Fonts (Space Grotesk,
Inter, JetBrains Mono)

## 2. Project Structure

```
sai_portfolio/
├── manage.py
├── portfolio/          # project config (settings, urls, wsgi, asgi)
├── core/                # the app: models, views, forms, admin, urls
├── templates/            # base.html, home.html, project_detail.html
├── static/css/style.css  # design system
├── static/js/main.js     # mode switch, typing effect, scroll reveal, filters
├── media/resumes/         # your two resume PDFs (already included)
├── populate.py             # seeds the DB with your real resume data
├── requirements.txt
└── .gitignore
```

## 3. Local Setup (Windows / PowerShell — matches your environment)

```powershell
# from inside the unzipped sai_portfolio folder
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser      # for /admin/ access

# seed real data (profile, skills, projects, experience, education, certs)
python manage.py shell < populate.py

python manage.py runserver
```

Open **http://127.0.0.1:8000/** for the site and
**http://127.0.0.1:8000/admin/** to manage content.

> If PowerShell blocks script execution (a recurring issue on your machine),
> run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that
> terminal session before installing, or activate via
> `venv\Scripts\activate.bat` in cmd.exe instead of PowerShell.

## 4. What's already seeded for you

`populate.py` loads your real resume content directly:

- **Projects**: AgriGro (Django e-commerce, live on Render), Employee
  Attrition Prediction (ML, 89.1% accuracy), Retail Sales EDA,
  Healthcare Appointment EDA, E-Commerce Power BI Dashboard
- **Skills**: grouped and tagged by track (SE-only, DA-only, or both) so the
  mode switch shows the right ones
- **Experience**: Data Science Intern (Dhaapps), Python Web Development
  Intern (ICT Academy)
- **Education**: B.Tech ECE (CGPA 8.5), Intermediate MPC (87%), SSC (CGPA 9.8)
- **Certifications**: all 4 from your resumes
- **Resumes**: both PDFs are already copied into `media/resumes/` and linked
  by the seed script — the Download Resume button switches file based on
  SE/DA mode automatically

To add a 6th project or edit any text, go to `/admin/` — no code changes
needed.

## 5. Adding real project screenshots

Project cards work fine without images (they show a styled category tag
instead). To add a real screenshot: open a project in `/admin/`, upload an
image to the **Image** field — it appears automatically on both the card and
detail page.

## 6. Deployment (Render / Railway)

1. Push this project to a GitHub repo (see step 7 below).
2. Set these environment variables on your host:
   - `DJANGO_SECRET_KEY` — generate a real one, don't reuse the dev key
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=yourdomain.onrender.com`
   - `DATABASE_URL` — provided automatically if you attach a Postgres add-on
   - (optional) `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`,
     `CONTACT_NOTIFY_EMAIL`, `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
     — only needed if you want contact-form email notifications
3. Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
4. Start command: `gunicorn portfolio.wsgi`
5. After first deploy, run once via the host's shell:
   `python manage.py createsuperuser` and
   `python manage.py shell < populate.py`

WhiteNoise is already wired up so static files (CSS/JS/fonts) serve correctly
in production without a separate CDN.

## 7. Pushing to GitHub (GitHub Desktop, matches your workflow)

1. Unzip this folder to `C:\Users\saiad\OneDrive\Desktop\protfolio\sai_protfolio` (or wherever you want it)
2. Open GitHub Desktop → **Add Local Repository** → select the folder
3. Commit all files, then **Publish repository**
4. `.gitignore` is already set up to exclude `db.sqlite3`, `__pycache__`, and
   uploaded certificate/project images — but keeps your resume PDFs, since
   those are meant to ship with the site

## 8. Notes on the design

- The **SE / DA switch** in the navbar is the whole point of this design —
  it's not a cosmetic toggle. It changes the accent color (indigo for SE,
  amber for DA), the hero headline and terminal-typing role, the resume file
  that downloads, and which skills/experience rows are visible.
- All animations respect `prefers-reduced-motion`.
- Fully responsive: mobile gets a full-screen nav drawer, single-column
  layouts, and stacked forms.
