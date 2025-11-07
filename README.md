# Collaborative Event & Task Planning API

A Django REST Framework project with JWT authentication and PostgreSQL.

---

## 🚀 Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/78RainDrops/collab-planner.git
cd collab-planner
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create `.env` file:

```env
DEBUG=True
DB_NAME=db
DB_USER=user
DB_PASSWORD=collab123
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. Create Superuser

```bash
python3 manage.py createsuperuser
```

### 7. Run Server

```bash
python3 manage.py runserver
```

### 8. Test Endpoints

Use Postman or cURL to test:

- `/api/accounts/register/`
- `/api/accounts/token/`
- `/api/accounts/refresh/`
- `/api/accounts/test/`

---

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT for authentication

---

## Current Progress

✅ Day 1: Setup Project
✅ Day 2: Database Config
✅ Day 3: Custom User Model
✅ Day 4: JWT Auth
✅ Day 5: Testing & Docs
