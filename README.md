# English Verbs Trainer

A backend-powered application for learning English irregular verbs.

The project includes:

* FastAPI backend
* Telegram bot as the first client
* SQLite database
* User progress tracking
* Scoring system
* Level-based training

---

## 🚀 Features

* Learn irregular verbs through training sessions
* Random verb selection
* Level-based training (A0, A1, etc.)
* Track user progress
* Score system (points for correct answers)
* Statistics and analytics
* Telegram bot interface

---

## 🏗 Project Structure

```
english-verbs-trainer/
│
├── app/
│   ├── main.py
│   ├── core/
│   ├── database/
│   ├── schemas/
│   ├── crud/
│   ├── services/
│   ├── api/
│   └── bot/
│
├── data/
│   └── irregular_verbs.json
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/english-verbs-trainer.git
cd english-verbs-trainer
```

### 2. Create virtual environment

```
python -m venv .venv
```

Activate it:

Windows:

```
.venv\Scripts\activate
```

Mac/Linux:

```
source .venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Create `.env` file

Copy `.env.example`:

```
cp .env.example .env
```

Fill in your Telegram bot token:

```
TELEGRAM_TOKEN=your_token_here
```

---

### 5. Initialize database

```
uvicorn app.main:app --reload
```

Then in another terminal:

```
python -m app.database.seed
```

---

## ▶️ Run the project

### Run API

```
uvicorn app.main:app --reload
```

API docs:

```
http://127.0.0.1:8000/docs
```

---

### Run Telegram bot

```
python -m app.bot.telegram_bot
```

---

## 🤖 Telegram Bot Commands

* `/start` — start the bot
* `/help` — show help
* `/train` — get a training task
* `/stats` — show statistics
* `/score` — show score
* `/progress` — show level progress

---

## 📊 API Endpoints

* `GET /verbs` — list all verbs
* `GET /verbs/{id}` — get verb by ID
* `GET /verbs/by-level/{level}` — verbs by level
* `GET /train/task` — get training task
* `GET /train/task?level=A0` — task by level
* `POST /train/check` — check answer
* `GET /stats/{user_id}` — user statistics
* `GET /progress/{user_id}/{level}` — level progress

---

## 🧠 Architecture

The project is designed as a scalable backend system:

* **FastAPI** — API layer
* **Services** — business logic
* **CRUD** — database operations
* **Telegram bot** — client interface
* **SQLite** — database

Future extensions:

* mobile application (Flutter / React Native)
* authentication (JWT)
* spaced repetition system
* gamification features

---

## 💡 Project Goal

This project demonstrates:

* backend architecture design
* API development
* database modeling
* integration with external services (Telegram)
* building scalable applications

---

## 📌 Status

✅ Core functionality implemented
🚧 Ready for deployment and further expansion

---
