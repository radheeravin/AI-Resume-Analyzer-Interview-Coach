def calculate_ats_score(resume_text: str, resume_skills: list, jd_skills: list) -> dict:
    """
    Calculates ATS score based on criteria:
    - Skill match (35%)
    - Keyword density (20%)
    - Formatting / sections / length proxy (45%)
    """
    # 1. Skill Match Score (Max 35)
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)
    
    if not jd_set:
        skill_score = 35.0
    else:
        skill_score = (len(resume_set & jd_set) / len(jd_set)) * 35.0
        
    # 2. Keyword Density (Max 20)
    # Check if jd skills appear frequently in text
    resume_lower = resume_text.lower()
    keyword_matches = sum(1 for skill in jd_set if skill in resume_lower)
    keyword_score = (keyword_matches / len(jd_set)) * 20.0 if jd_set else 20.0
    
    # 3. Resume length & Formatting proxy (Max 45)
    # A standard resume should have > 200 words
    word_count = len(resume_text.split())
    format_score = min(45.0, (word_count / 300) * 45.0) 
    
    total_score = skill_score + keyword_score + format_score
    
    return {
        "ATS Score": round(total_score, 1),
        "Breakdown": {
            "Skill Match (35%)": round(skill_score, 1),
            "Keyword Density (20%)": round(keyword_score, 1),
            "Formatting & Relevance (45%)": round(format_score, 1)
        }
    }
