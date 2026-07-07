import streamlit as st
import requests

st.set_page_config(page_title="Interview Coach", page_icon="🎤", layout="wide")

st.title("🎤 AI Interview Coach")
st.write("Generate tailored interview questions and practice with AI voice evaluation.")

# Form to generate questions
with st.expander("📝 Step 1: Generate Questions", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input("Target Role", value="Software Engineer")
        resume_skills_input = st.text_input("Your Skills (comma-separated)", value="Python, SQL")
    with col2:
        jd_skills_input = st.text_input("Job Required Skills (comma-separated)", value="AWS, Docker")
        num_q = st.slider("Number of Questions", min_value=1, max_value=10, value=3)

    if st.button("Generate Questions"):
        with st.spinner("Generating..."):
            try:
                payload = {
                    "role": role,
                    "resume_skills": [s.strip() for s in resume_skills_input.split(",") if s.strip()],
                    "jd_skills": [s.strip() for s in jd_skills_input.split(",") if s.strip()],
                    "num_questions": num_q
                }
                res = requests.post("http://127.0.0.1:8000/api/v1/generate_questions", json=payload)
                if res.status_code == 200 and res.json().get("status") == "success":
                    st.session_state["interview_questions"] = res.json()["questions"]
                    st.success("Questions generated successfully!")
                else:
                    st.error("Failed to generate questions.")
            except Exception as e:
                st.error(f"Connection error: {e}. Is the backend running?")

if "interview_questions" in st.session_state:
    st.subheader("💡 Your Interview Questions")
    
    # Choose a question to answer
    selected_q = st.selectbox("Select a question to practice:", st.session_state["interview_questions"])
    
    st.write("---")
    st.subheader("🎤 Record Your Answer")
    
    # Using Streamlit's native audio input
    audio_value = st.audio_input("Speak your answer clearly:")
    
    if audio_value is not None:
        if st.button("Evaluate My Answer", type="primary"):
            with st.spinner("Transcribing and evaluating... (This may take a moment depending on your hardware)"):
                try:
                    files = {"audio_file": ("answer.wav", audio_value.getvalue(), "audio/wav")}
                    data = {"question": selected_q}
                    res = requests.post("http://127.0.0.1:8000/api/v1/evaluate_audio", files=files, data=data)
                    
                    if res.status_code == 200:
                        result = res.json()
                        if result["status"] == "success":
                            st.success("Evaluation Complete!")
                            
                            st.write("**Your Transcript:**")
                            st.info(result["transcript"] if result["transcript"] else "No speech detected.")
                            
                            eval_data = result["evaluation"]
                            st.metric(label="Confidence & Quality Score", value=f"{eval_data['score']}/100")
                            
                            st.write("**Feedback:**")
                            st.markdown(eval_data["feedback"])
                            
                            if eval_data["filler_words"]:
                                st.warning(f"Filler words detected: {', '.join(eval_data['filler_words'])}")
                        else:
                            st.error(f"Error: {result['message']}")
                    else:
                        st.error(f"Backend error: {res.status_code}")
                except Exception as e:
                    st.error(f"Connection error: {e}")
