# Task Management (Django)

A small, straightforward Task Management web app built with Django. It’s intentionally simple: you can create tasks, view them, update them, mark them as done, and delete them without any user accounts, login, or authentication.

Because there’s **no authentication**, everything is shared and public for anyone who can access the site.

---

## Features

- Add a new task
- View task list
- View task details (if implemented)
- Update/edit tasks
- Mark tasks as completed (and optionally undo)
- Delete tasks

---

## Tech stack

- Python
- Django
- SQLite (default local database)
- Django Templates (server-rendered HTML)

---

## Requirements (`requirements.txt`)

This project should include a `requirements.txt` file so anyone can install the same dependencies quickly.

### Install dependencies

```bash name=terminal
pip install -r requirements.txt
```

### If `requirements.txt` is missing
You can generate it after installing your dependencies:

```bash name=terminal
pip freeze > requirements.txt
```

### Typical `requirements.txt` content (example)
Your exact versions may differ, but a minimal file often looks like:

```text name=requirements.txt
Django>=4.2,<6.0
```

If you are using extra packages (crispy forms, django-filter, etc.), they should appear here too.

---

## Data model (Models)

This app centers on a single model: **Task**.

A clean, typical version of the model looks like this (adjust field names to match your code):

```python name=app/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

---

## Run locally

### 1) Create and activate a virtual environment

**Windows (PowerShell):**
```bash name=terminal
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash name=terminal
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash name=terminal
pip install -r requirements.txt
```

### 3) Migrate database

```bash name=terminal
python manage.py makemigrations
python manage.py migrate
```

### 4) Start server

```bash name=terminal
python manage.py runserver
```

Open: http://127.0.0.1:8000/

---

## Django admin (optional)

Create an admin user:
```bash name=terminal
python manage.py createsuperuser
```

Admin panel:
- http://127.0.0.1:8000/admin/

Registering the model (typical):

```python name=app/admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "created_at", "updated_at")
    list_filter = ("completed",)
    search_fields = ("title", "description")
```

---

## Notes / limitations

- No authentication or user separation
- Not production-ready as-is (no permissions)

---

# Author
GitHub: `kawser25350`
