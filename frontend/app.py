import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer & Interview Coach",
    page_icon="📄",
    layout="wide"
)

st.title("Welcome to AI Resume Analyzer & Interview Coach 🚀")

st.markdown("""
This platform helps you optimize your resume for ATS and prepare for technical interviews using AI.

### 🌟 Features:
- **Resume Analyzer:** Upload your PDF resume, paste the Job Description, and get an ATS match score with a skill gap analysis.
- **Interview Coach:** Practice mock interviews with AI-generated questions tailored to your profile and the target role.
- **Voice Evaluation:** Answer questions using your microphone and receive instant feedback on confidence, technical depth, and communication skills.

👈 **Select a page from the sidebar to get started!**
""")

st.info("Note: To fully utilize the AI features, make sure your OPENAI_API_KEY is configured in the `.env` file.")
