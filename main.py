from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import resume

app = FastAPI(
    title="AI Resume Coach",
    description="AI-powered resume analyzer, job matcher, and interview question generator using Claude AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)

@app.get("/")
async def root():
    return {
        "message": "AI Resume Coach",
        "version": "1.0.0",
        "docs": "/docs",
        "features": [
            "Resume Analysis & ATS Scoring",
            "Job Description Matching",
            "Interview Question Generation"
        ]
    }
