from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
import tempfile
import os

from ai_engine.resume_parser import parse_resume
from ai_engine.ats_score import calculate_ats_score
from ai_engine.skill_gap import analyze_skill_gap

router = APIRouter()

@router.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description_skills: str = Form("")
):
    """
    Upload a resume (PDF) and provide optional Job Description skills (comma-separated)
    to get an ATS score and skill gap analysis.
    """
    # 1. Save uploaded file temporarily
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # 2. Parse Resume
        parsed_data = parse_resume(tmp_path)
        resume_skills = parsed_data["parsed_data"]["skills"]
        resume_text = parsed_data["raw_text"]

        # 3. Process JD Skills
        jd_skills_list = [s.strip() for s in job_description_skills.split(",")] if job_description_skills else []

        # 4. ATS Score & Skill Gap
        ats_result = calculate_ats_score(resume_text, resume_skills, jd_skills_list)
        skill_gap = analyze_skill_gap(resume_skills, jd_skills_list)

        return {
            "status": "success",
            "parsed_data": parsed_data["parsed_data"],
            "ats_result": ats_result,
            "skill_gap": skill_gap
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)
