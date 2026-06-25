from pydantic import BaseModel
from typing import Optional, List

class ResumeAnalysis(BaseModel):
    ats_score: float
    overall_score: float
    strengths: List[str]
    weaknesses: List[str]
    missing_keywords: List[str]
    suggestions: List[str]
    summary: str

class InterviewQuestions(BaseModel):
    technical: List[str]
    behavioral: List[str]
    role_specific: List[str]

class JobMatch(BaseModel):
    match_percentage: float
    matching_skills: List[str]
    missing_skills: List[str]
    recommendation: str
