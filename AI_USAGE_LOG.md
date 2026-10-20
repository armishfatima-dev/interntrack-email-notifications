# AI Usage Log - Week 4: External Email Integration & Background Notifications

## Task Summary

Integrated the Resend transactional email API asynchronously using Python's `httpx` and FastAPI's `BackgroundTasks` to notify interns when their work is graded.

## 1. What was asked?

- Architect a non-blocking email notification service using an external provider.
- Enforce secret safety, explicit timeouts (5.0s), error handling, and robust logger output.

## 2. What was generated?

- Created `app/services/notifications.py` handling asynchronous HTTP requests with exception safety.
- Wired FastAPI `BackgroundTasks` into the submission grading endpoint.
- Configured `.env` and `.gitignore` rules to prevent credential leaks.

## 3. What was manually verified or changed, and why?

- **Timeout Management:** Verified that `httpx.AsyncClient(timeout=5.0)` prevents slow network calls from hanging server threads.
- **Security Check:** Ensured `.env` is properly registered in `.gitignore` to avoid exposing API keys on GitHub.
- **Resilience Testing:** Tested behavior when API keys are missing/invalid; confirmed the API returns `200 OK` instantly while logging errors server-side.
