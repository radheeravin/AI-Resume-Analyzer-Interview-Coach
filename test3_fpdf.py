from reports.generator import generate_pdf_report
import traceback

sample_ats = {
    "ATS Score": 82,
    "Breakdown": {
        "Skill Match (35%)": 28,
        "Keyword Density (20%)": 18,
        "Formatting & Relevance (45%)": 36
    }
}

sample_gap = {
    "match_percentage": 80.0,
    "matched_skills": ["Python", "SQL", "Machine Learning"],
    "missing_skills": ["AWS", "Docker", "FastAPI"]
}

try:
    generate_pdf_report(sample_ats, sample_gap, filepath="reports/test_full.pdf")
    print("SUCCESS")
except Exception as e:
    traceback.print_exc()
