High-level plan (milestones)

Project & repo setup (virtualenv, requirements, Django project, billing app). — starting now

Base settings (Postgres-ready, static/media, auth, third-party keys placeholders).

Core models, migrations, admin.

Registration forms/pages + file upload handling.

RADIUS integration helper (radcheck SQL write).

Voucher generation, plan management, dashboard views.

M-Pesa Daraja integration (checkout + callback).

WhatsApp delivery (Twilio/Meta) utils & templates.

RouterOS helpers & script assistant.

Docker Compose for local dev (web, db, redis, freeradius).

Celery tasks for background jobs.

Testing, security hardening, deployment notes.

I’ll deliver concrete files/commands for each milestone. Now I’m starting Milestone 1: Project & repo setup.

Milestone 1 — Project & repo setup (what I'll create now)

requirements.txt

Commands to create virtualenv and Django project

Project layout (folders & files)

settings.py minimal changes (static, media, installed apps)

Create billing app with initial models.py (we already discussed model shapes — I'll include a cleaned starter)

Initial urls.py and wsgi.py snippets

Instructions to run migrations and start dev server
