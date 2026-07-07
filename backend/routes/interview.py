from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from typing import List
import tempfile
import os

from ai_engine.interview_generator import generate_interview_questions
from ai_engine.audio_utils import transcribe_audio
from ai_engine.confidence_analysis import evaluate_interview_response

router = APIRouter()

class InterviewRequest(BaseModel):
    resume_skills: List[str]
    jd_skills: List[str]
    role: str = "Software Engineer"
    num_questions: int = 5

@router.post("/generate_questions")
def generate_questions(request: InterviewRequest):
    try:
        questions = generate_interview_questions(
            request.resume_skills,
            request.jd_skills,
            request.role,
            request.num_questions
        )
        return {"status": "success", "questions": questions}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.post("/evaluate_audio")
async def evaluate_audio(
    question: str = Form(...),
    audio_file: UploadFile = File(...)
):
    try:
        suffix = os.path.splitext(audio_file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await audio_file.read())
            tmp_path = tmp.name

        # Transcribe
        transcript = transcribe_audio(tmp_path)
        
        # Evaluate
        evaluation = evaluate_interview_response(question, transcript)
        
        return {
            "status": "success",
            "transcript": transcript,
            "evaluation": evaluation
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)
