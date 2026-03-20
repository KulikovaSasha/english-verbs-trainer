# English Verbs Trainer

Backend service for learning English irregular verbs with support for Telegram bot and future mobile application.

---

## 🚀 Project Overview

This project is a backend platform for practicing English irregular verbs.

It provides:

* training sessions with verbs
* answer validation
* user progress tracking
* statistics and performance analysis

The system is designed with scalability in mind:

* Telegram bot (first client)
* REST API (core backend)
* Mobile application (future client)

---

## 🏗️ Architecture

```
Mobile App (future)
        |
        | HTTP API
        |
Telegram Bot
        |
     FastAPI
        |
    Database
```

---

## 📂 Project Structure

```
english-verbs-trainer/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   │
│   ├── core/               # Configuration
│   │   └── config.py
│   │
│   ├── database/           # Database layer
│   │   ├── db.py
│   │   ├── models.py
│   │   └── seed.py
│   │
│   ├── schemas/            # Pydantic schemas
│   │   └── verb.py
│   │
│   ├── crud/               # Database operations
│   │   ├── user.py
│   │   ├── verb.py
│   │   └── progress.py
│   │
│   ├── services/           # Business logic
│   │   └── trainer.py
│   │
│   ├── api/                # API routes
│   │   └── routes.py
│   │
│   └── bot/                # Telegram bot
│       ├── telegram_bot.py
│       └── handlers.py
│
├── data/
│   └── irregular_verbs.json
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── .python-version
```

---

## ⚙️ Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite (for development)
* python-dotenv
* python-telegram-bot (planned)
* httpx

---

## 🔧 Installation

### 1. Clone repository

```
git clone https://github.com/KulikovaSasha/english-verbs-trainer.git
cd english-verbs-trainer
```

---

### 2. Create virtual environment

```
python -m venv .venv
```

Activate it:

**Windows:**

```
.venv\Scripts\activate
```

**Mac/Linux:**

```
source .venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create `.env` file:

```
TELEGRAM_TOKEN=
DATABASE_URL=sqlite:///./verbs.db
```

---

## ▶️ Run the project

```
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

* Root:

```
GET /
```

Response:

```
{"message": "English Verbs Trainer API is running"}
```

* Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🗄️ Database

SQLite database is used for development.

The database file:

```
verbs.db
```

Tables:

* users
* irregular_verbs
* training_results
* user_progress

---

## 📊 Features (planned)

* Training sessions
* Answer validation
* User statistics
* Difficulty tracking
* Levels (A0, A1, A2...)
* Streak system
* Telegram bot interface
* Mobile app integration

---

## 🧠 Development Plan

### Day 1

* Project setup
* FastAPI
* Database models

### Day 2

* Load verbs from JSON
* CRUD operations
* Basic API

### Day 3+

* Training logic
* Telegram bot
* Statistics
* Game mechanics

---

## 🔐 Environment Variables

| Variable       | Description                |
| -------------- | -------------------------- |
| TELEGRAM_TOKEN | Telegram bot token         |
| DATABASE_URL   | Database connection string |

---

## 🧩 Future Improvements

* PostgreSQL support
* Authentication (JWT)
* Docker support
* CI/CD pipeline
* Mobile app (Flutter / React Native)

---

## 👨‍💻 Author

Backend project for learning and practicing Python + FastAPI development.

---
