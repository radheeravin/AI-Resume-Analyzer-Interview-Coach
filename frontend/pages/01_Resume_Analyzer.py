import streamlit as st
import requests

st.set_page_config(page_title="Resume Analyzer", page_icon="📈", layout="wide")

st.title("📈 AI Resume Analyzer")
st.write("Upload your resume and the target job description to get your ATS score and skill gap analysis.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Upload Resume")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

with col2:
    st.subheader("2. Job Description")
    jd_skills = st.text_area("Enter required skills (comma-separated)", placeholder="e.g., Python, AWS, Docker, Machine Learning")

if st.button("Analyze Resume", type="primary"):
    if uploaded_file is not None:
        with st.spinner("Analyzing your resume..."):
            try:
                # Prepare the request
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                data = {"job_description_skills": jd_skills}
                
                # Send to FastAPI backend
                response = requests.post("http://127.0.0.1:8000/api/v1/analyze_resume", files=files, data=data)
                
                if response.status_code == 200:
                    result = response.json()
                    if result["status"] == "success":
                        st.success("Analysis Complete!")
                        
                        # Display Results
                        res_col1, res_col2 = st.columns([1, 1])
                        
                        with res_col1:
                            st.subheader("📊 ATS Score")
                            ats = result["ats_result"]
                            st.metric(label="Overall Score", value=f"{ats['ATS Score']}/100")
                            
                            st.write("**Score Breakdown:**")
                            for key, val in ats["Breakdown"].items():
                                st.write(f"- {key}: {val}")
                                
                        with res_col2:
                            st.subheader("🛠️ Skill Gap Analysis")
                            gap = result["skill_gap"]
                            st.metric(label="Skill Match", value=f"{gap['match_percentage']}%")
                            
                            st.write("**Matched Skills:**")
                            st.success(", ".join(gap["matched_skills"]) if gap["matched_skills"] else "None")
                            
                            st.write("**Missing Skills (Add these!):**")
                            st.error(", ".join(gap["missing_skills"]) if gap["missing_skills"] else "None")
                            
                        st.subheader("Extracted Details")
                        st.json(result["parsed_data"])
                    else:
                        st.error(f"Error: {result.get('message', 'Unknown error')}")
                else:
                    st.error(f"Backend returned status code: {response.status_code}")
            except Exception as e:
                st.error(f"Connection error: {e}. Is the backend running at 127.0.0.1:8000?")
    else:
        st.warning("Please upload a resume first.")
