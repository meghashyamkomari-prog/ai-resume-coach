cd /tmp/ai-resume-remote
cat > README.md << 'EOF'
# AI Resume Coach
AI-powered career tool that analyzes resumes, matches job descriptions, 
and generates personalized interview questions using Claude AI.

## Architecture
PDF Resume → FastAPI → PyPDF2 Extraction → Claude AI Analysis → JSON Results

## Tech Stack
* Python, FastAPI, SQLAlchemy, Pydantic
* Claude AI (Anthropic) for resume analysis
* PyPDF2 for PDF text extraction
* Swagger UI (API documentation)

## Features
* Analyzes resume and generates ATS compatibility score
* Identifies missing keywords for target roles
* Matches resume against job descriptions
* Generates role-specific interview questions
* Provides actionable improvement suggestions
* REST API with full Swagger documentation

## Sample Results
Real analysis on Data Engineer resume:
✅ ATS Score: 8.7/10
✅ Overall Score: 8.4/10
✅ 5 key strengths identified
✅ Missing keywords detected (Terraform, CI/CD, Delta Lake)
✅ 5 actionable improvement suggestions

## API Endpoints
* POST /resume/analyze - Analyze resume PDF
* POST /resume/match-job - Match resume to job description
* POST /resume/interview-questions - Generate interview questions
* GET /resume/health - Health check

## How to Run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8003
# Navigate to http://127.0.0.1:8003/docs
```

## Project Structure
ai-resume-coach/
├── main.py              # FastAPI application
├── routers/
│   └── resume.py       # API route definitions
├── services/
│   ├── analyzer.py     # Resume analysis & job matching
│   └── interview.py    # Interview question generation
└── schemas/
    └── models.py       # Pydantic data models

## Use Cases
* Job seekers optimizing resumes for ATS systems
* Career coaches providing data-driven feedback
* Recruiters screening candidates efficiently
* Engineers preparing for technical interviews
EOF
git add README.md
git commit -m "docs: Add comprehensive README"
git push
