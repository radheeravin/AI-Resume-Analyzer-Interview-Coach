import streamlit as st
import os
import sys

# Ensure backend and ai_engine can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

st.set_page_config(page_title="Download Report", page_icon="📄", layout="wide")

st.title("📄 Final Analysis Report")
st.write("Generate and download a comprehensive PDF report of your ATS score and skill gaps.")

st.info("In a full production flow, this page would fetch your latest analysis from the Supabase database. For this MVP, you can generate a sample report based on dummy data or session state.")

if st.button("Generate PDF Report", type="primary"):
    with st.spinner("Generating PDF..."):
        from reports.generator import generate_pdf_report
        
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
        
        filepath = generate_pdf_report(sample_ats, sample_gap)
        
        if os.path.exists(filepath):
            st.success("PDF Generated Successfully!")
            with open(filepath, "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(label="📥 Download Report",
                               data=PDFbyte,
                               file_name="AI_Resume_Report.pdf",
                               mime='application/octet-stream')
