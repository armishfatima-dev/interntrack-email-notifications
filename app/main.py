from fastapi import FastAPI
from app.database import engine, Base
from app.routers import submissions

# Create database tables automatically on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Interntrack API - Week 4", version="1.0.0")

# Include routers
app.include_router(submissions.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Interntrack Backend API - Week 4 is running successfully!"}

