# Interntrack Backend - Week 4: External Email Integration & Asynchronous Notifications

## Overview

This repository contains the Week 4 implementation for the Interntrack Backend. It introduces a resilient, non-blocking email notification service that alerts interns when their submissions are graded or when a new week unlocks.

## Features

- **Asynchronous Execution:** Utilizes FastAPI `BackgroundTasks` to send email notifications without delaying HTTP responses.
- **Resilient Third-Party API Integration:** Leverages `httpx` with explicit 5.0-second timeouts and exception handling (`try/except`) to prevent server hangs.
- **Secure Secret Management:** Loads API keys securely via environment variables (`.env`), keeping sensitive credentials out of version control.
- **Audit Logging:** Integrates Python standard logging to capture email delivery statuses and errors.

## Project Structure

interntrack-email-notifications/
│
├── app/
│ ├── database.py
│ ├── main.py
│ ├── models/
│ │ └── models.py
│ ├── routers/
│ │ ├── admin.py
│ │ ├── auth.py
│ │ └── submissions.py
│ ├── schemas/
│ │ └── schemas.py
│ └── services/
│ ├── auth.py
│ ├── rbac.py
│ └── notifications.py
│
├── .env
├── .env.example
├── .gitignore
├── AI_USAGE_LOG.md
└── README.md

## Setup & Running Locally

1. Activate virtual environment and install dependencies:
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv httpx

2. Configure local environment variables:
   Copy .env.example to .env and fill in your credentials.

3. Start the FastAPI server:
   uvicorn app.main:app --reload
