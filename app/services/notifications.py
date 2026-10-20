import os
import logging
import httpx

logger = logging.getLogger("notifications")
logging.basicConfig(level=logging.INFO)

EMAIL_API_KEY = os.getenv("EMAIL_API_KEY", "")
EMAIL_FROM = os.getenv("EMAIL_FROM", "onboarding@resend.dev")
RESEND_URL = "https://api.resend.com/emails"

async def send_email_notification(to_email: str, subject: str, content: str):
    """
    Sends an email notification using Resend API asynchronously.
    Wrapped in try/except with explicit timeouts to ensure non-blocking background execution.
    """
    if not EMAIL_API_KEY:
        logger.warning(f"EMAIL_API_KEY not set. Mocking email send to {to_email} with subject: '{subject}'")
        return

    headers = {
        "Authorization": f"Bearer {EMAIL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": EMAIL_FROM,
        "to": [to_email],
        "subject": subject,
        "html": f"<p>{content}</p>"
    }

    try:
        # Enforce 5.0 second timeout to prevent hanging connections
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(RESEND_URL, json=payload, headers=headers)
            
            if response.status_code in (200, 201):
                logger.info(f"Email successfully sent to {to_email}. Provider response: {response.json()}")
            else:
                logger.error(f"Failed to send email to {to_email}. Status: {response.status_code}, Body: {response.text}")
                
    except httpx.TimeoutException:
        logger.error(f"Timeout occurred while attempting to send email to {to_email}.")
    except Exception as e:
        logger.error(f"Unexpected error sending email to {to_email}: {str(e)}")

