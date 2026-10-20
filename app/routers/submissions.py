from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Submission, User
from app.schemas.schemas import GradeUpdateSchema
from app.services.auth import require_role # Or your existing role dependency
from app.services.notifications import send_email_notification

router = APIRouter(prefix="/submissions", tags=["Submissions"])

@router.patch("/{submission_id}/grade")
async def grade_submission(
    submission_id: int,
    grade_data: GradeUpdateSchema,
    background_tasks: BackgroundTasks, # <-- 1. Inject BackgroundTasks here
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["mentor", "admin"]))
):
    # Fetch submission
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
        
    # Update grade and feedback
    submission.grade = grade_data.grade
    submission.feedback = grade_data.feedback
    db.commit()
    db.refresh(submission)
    
    # 2. Trigger asynchronous background notification
    intern_email = submission.intern.email
    subject = f"Your submission for Week {submission.week} has been graded!"
    content = f"Hello {submission.intern.name},<br>Your submission received grade: <strong>{submission.grade}</strong>.<br>Feedback: {submission.feedback}"
    
    background_tasks.add_task(
        send_email_notification,
        to_email=intern_email,
        subject=subject,
        content=content
    )
    
    # 3. Returns immediately without waiting for the email provider
    return {
        "message": "Submission graded successfully and email queued in background.",
        "submission_id": submission.id,
        "grade": submission.grade
    }

