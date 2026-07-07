from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

def generate_interview_questions(resume_skills: list, jd_skills: list, role: str = "Software Engineer", num_questions: int = 5) -> list:
    """
    Generate technical interview questions based on candidate skills and job description.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your_openai_api_key_here":
        # Fallback dummy questions if API key is not set
        return [
            f"Explain how you have used {resume_skills[0] if resume_skills else 'Python'} in your previous projects.",
            f"What is your experience with {jd_skills[0] if jd_skills else 'cloud technologies'}?",
            "Can you describe a time you faced a difficult technical challenge?",
            "How do you ensure your code is scalable and maintainable?",
            "Describe your understanding of system design for high-traffic applications."
        ]

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key=openai_api_key)
    
    prompt = PromptTemplate(
        input_variables=["role", "resume_skills", "jd_skills", "num_questions"],
        template="""
        You are an expert technical interviewer for a {role} position.
        The candidate has the following skills: {resume_skills}.
        The job requires the following skills: {jd_skills}.
        
        Generate {num_questions} technical interview questions that assess the candidate's 
        knowledge based on their skills and the job requirements. Include a mix of conceptual 
        and scenario-based questions.
        
        Return the questions as a numbered list.
        """
    )
    
    chain = prompt | llm
    
    response = chain.invoke({
        "role": role,
        "resume_skills": ", ".join(resume_skills),
        "jd_skills": ", ".join(jd_skills),
        "num_questions": num_questions
    })
    
    # Process the output text into a list
    questions = response.content.split('\n')
    questions = [q.strip() for q in questions if q.strip() and q[0].isdigit()]
    return questions
