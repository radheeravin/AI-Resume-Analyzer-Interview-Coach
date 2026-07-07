# AI Resume Analyzer & Interview Coach

An end-to-end GenAI application that parses resumes, evaluates skill relevance, and provides an AI-driven mock interview experience.

## Features

- **Resume Parsing:** Extract skills, education, experience using NLP (spaCy) and PyMuPDF.
- **ATS Scoring:** Calculate ATS match score based on job description.
- **AI Skill Gap Analysis:** Detect missing skills and suggest improvements.
- **AI Mock Interview:** Generate technical questions based on candidate profile.
- **Voice Interview Evaluation:** Real-time speech-to-text (Whisper) and confidence analysis.

## Architecture Diagram

*(Coming Soon)*

## Installation Steps

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Download spaCy model: `python -m spacy download en_core_web_sm`
6. Set up `.env` with `OPENAI_API_KEY` and `SUPABASE_URL`/`KEY`.
7. Run Backend: `uvicorn backend.main:app --reload`
8. Run Frontend: `streamlit run frontend/app.py`

## API Documentation

*(Coming Soon)*

## Demo Video

*(Coming Soon)*
