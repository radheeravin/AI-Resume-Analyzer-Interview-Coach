def analyze_skill_gap(resume_skills: list, jd_skills: list) -> dict:
    """
    Compares resume skills with Job Description skills and identifies missing ones.
    """
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)
    
    missing_skills = list(jd_set - resume_set)
    matched_skills = list(jd_set & resume_set)
    
    match_percentage = (len(matched_skills) / len(jd_set)) * 100 if jd_set else 100.0
    
    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": [s.title() if len(s) > 3 else s.upper() for s in matched_skills],
        "missing_skills": [s.title() if len(s) > 3 else s.upper() for s in missing_skills]
    }
