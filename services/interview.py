import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_questions(resume_text: str, job_title: str) -> dict:
    prompt = f"""
You are an expert technical interviewer.

Based on this resume and job title, generate interview questions:

RESUME:
{resume_text[:2000]}

JOB TITLE: {job_title}

Respond in this EXACT JSON format:
{{
    "technical": [
        "Technical question 1?",
        "Technical question 2?",
        "Technical question 3?",
        "Technical question 4?",
        "Technical question 5?"
    ],
    "behavioral": [
        "Behavioral question 1?",
        "Behavioral question 2?",
        "Behavioral question 3?"
    ],
    "role_specific": [
        "Role specific question 1?",
        "Role specific question 2?",
        "Role specific question 3?"
    ]
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
