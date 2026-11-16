# Django Polling/Voting Application

A classroom-ready Django project demonstrating models, migrations, URL routing, views, forms, templates, admin data management, CSRF protection, validation, and sample data.

## Requirements
- Python 3.10+
- Django 5.2.x (`requirements.txt`)

## Run locally (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations polls
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata polls/fixtures/sample_polls.json
python manage.py runserver
```
If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal and activate again. Or use Command Prompt: `.venv\Scripts\activate.bat`.

Open:
- Poll application: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Log in to admin with the superuser credentials you created. Fixture data can be loaded after migrations. If you load it after creating a question manually, the sample questions will be added too.

## Main routes
| Route | Name | Purpose |
|---|---|---|
| `/` | `polls:index` | List open polls |
| `/<question_id>/` | `polls:detail` | Show a poll and vote form |
| `/<question_id>/vote/` | `polls:vote` | Validate and record a POST vote |
| `/<question_id>/results/` | `polls:results` | Show totals and percentages |
| `/admin/` | Django admin | Manage questions and choices |

## Security and validation
- Django template forms include `{% csrf_token %}`.
- The vote endpoint accepts POST only (`@require_POST`).
- `VoteForm` limits choices to the current question and validates submitted data.
- Django's ORM is used instead of string-built SQL.
- Authentication is required for admin; create a strong superuser password.
- `DEBUG=True` and the development secret key are for local classroom use only. Before deployment, set `DEBUG=False`, use an environment-provided secret key, configure `ALLOWED_HOSTS`, and use HTTPS.

## Important limitation
This basic assignment app records votes but does not prevent one person from voting repeatedly. Preventing duplicate votes requires a defined identity policy (for example, authenticated users plus a unique constraint) and is outside this basic demonstration.

## Screenshots for submission
Run the project and capture real screenshots (Windows: `Win + Shift + S`) of:
1. Home page showing sample polls.
2. Poll detail page with options.
3. Results page after voting.
4. Django admin question list/edit screen.
5. Terminal showing `python manage.py runserver` running.

Save them in `screenshots/` and insert them into the report document. Do not submit placeholder screenshots as if they were real application output.
