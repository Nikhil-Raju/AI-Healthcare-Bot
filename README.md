# Nikhil AI – Healthcare Intelligence Bot

## Overview

Nikhil AI is a Django-based AI healthcare assistant that allows users to log in, ask medical-related questions, and receive AI-powered responses. The system stores each query and AI response in a database so users can review their past interactions.

The application integrates OpenAI GPT models to generate intelligent responses and provides quick links to hospitals and pharmacy resources.

---

# Features

* User Authentication (Signup, Login, Logout)
* AI-powered medical query analysis
* Modern chat interface
* Patient query history tracking
* Quick links to nearby hospitals and pharmacies
* Admin panel for managing user data and history
* Secure API integration using environment variables

---

# Technology Stack

## Backend

* Python
* Django Framework
* OpenAI API

## Frontend

* HTML
* Tailwind CSS
* JavaScript (Fetch API)

## Database

* SQLite (default Django database)

---

# Project Structure

```
HealthcareBot/
│
├── HealthcareBot/
│   ├── settings.py
│   ├── urls.py
│
├── bot_app/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── migrations/
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── index.html
│
├── db.sqlite3
└── manage.py
```

---

# Installation Guide

## 1. Clone the Repository

```
git clone https://github.com/yourusername/nikhil-ai-healthcare-bot.git
cd nikhil-ai-healthcare-bot
```

---

## 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

For Windows:

```
venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install django openai python-dotenv
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory.

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 5. Apply Database Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Create Admin User

```
python manage.py createsuperuser
```

---

## 7. Run the Server

```
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

---

# Application Workflow

1. User signs up for an account.
2. User logs in to the system.
3. User enters symptoms or medical questions.
4. The system sends the query to the OpenAI model.
5. AI generates a response.
6. The query and response are stored in the database.
7. The user can view previous searches from the sidebar.

---

# API Endpoint

### Chat API

```
GET /api/chat/?text=your_query
```

Example Response

```
{
 "reply": "AI generated medical response",
 "is_health": true,
 "h_link": "hospital search link",
 "p_link": "pharmacy search link"
}
```

---

# URL Routes

* `/login/` – User login
* `/signup/` – User registration
* `/chat/` – Chat interface
* `/logout/` – Logout
* `/api/chat/` – AI chat API

---

# Admin Panel

The Django admin panel allows administrators to view user queries and search history.

Access it here:

```
http://127.0.0.1:8000/admin
```

---

# Future Improvements

* Voice-based medical queries
* Medical dataset integration
* Doctor appointment booking
* Health report upload and analysis
* Multi-language support
* AI symptom prediction

---

# Disclaimer

This system is not a substitute for professional medical advice. Users should consult certified healthcare professionals for diagnosis and treatment.

---

# Author

Nikhil Raju
AI Healthcare Assistant built using Django and OpenAI.

