from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.analyzer import analyze_resume, match_job
from services.interview import generate_questions
import PyPDF2
import io

router = APIRouter(prefix="/resume", tags=["resume"])

def extract_text(file_bytes: bytes) -> str:
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"PDF extraction failed: {str(e)}")

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    resume_text = extract_text(content)
    result = analyze_resume(resume_text)
    return result

@router.post("/match-job")
async def match(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    content = await file.read()
    resume_text = extract_text(content)
    result = match_job(resume_text, job_description)
    return result

@router.post("/interview-questions")
async def interview(
    file: UploadFile = File(...),
    job_title: str = Form(...)
):
    content = await file.read()
    resume_text = extract_text(content)
    result = generate_questions(resume_text, job_title)
    return result

@router.get("/health")
async def health():
    return {"status": "healthy", "service": "AI Resume Coach"}
