import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_resume(resume_text: str) -> dict:
    prompt = f"""
You are an expert ATS resume analyzer and career coach.

Analyze this resume and provide a detailed assessment:

RESUME:
{resume_text[:3000]}

Respond in this EXACT JSON format:
{{
    "ats_score": 8.5,
    "overall_score": 8.0,
    "strengths": ["strength 1", "strength 2", "strength 3"],
    "weaknesses": ["weakness 1", "weakness 2"],
    "missing_keywords": ["keyword1", "keyword2", "keyword3"],
    "suggestions": ["suggestion 1", "suggestion 2", "suggestion 3"],
    "summary": "Brief 2-3 sentence summary of the resume"
}}

Return ONLY the JSON. No markdown. No backticks.
"""
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    import json
    return json.loads(message.content[0].text)

def match_job(resume_text: str, job_description: str) -> dict:
    prompt = f"""
You are an expert recruiter analyzing resume-job fit.

RESUME:
{resume_text[:2000]}

JOB DESCRIPTION:
{job_description[:2000]}

Respond in this EXACT JSON format:
{{
    "match_percentage": 85.0,
    "matching_skills": ["skill1", "skill2", "skill3"],
    "missing_skills": ["skill1", "skill2"],
    "recommendation": "Brief recommendation in 2-3 sentences"
}}

Return ONLY the JSON. No markdown. No backticks.
"""
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    import json
    return json.loads(message.content[0].text)
