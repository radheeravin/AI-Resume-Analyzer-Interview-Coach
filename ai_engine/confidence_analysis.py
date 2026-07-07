import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def evaluate_interview_response(question: str, transcript: str) -> dict:
    """
    Evaluates the transcribed audio answer based on technical depth, 
    communication skills, and generates a confidence score.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your_openai_api_key_here":
        return {
            "score": 85,
            "feedback": "Great response (Mocked). Make sure to mention specific tools.",
            "filler_words": ["uh", "umm"]
        }
        
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, openai_api_key=openai_api_key)
    
    prompt = PromptTemplate(
        input_variables=["question", "transcript"],
        template="""
        You are an expert technical interviewer evaluating a candidate's verbal response.
        
        Question Asked: {question}
        Candidate's Transcript: {transcript}
        
        Analyze the transcript for:
        1. Technical Correctness & Depth
        2. Communication quality (clarity, structure)
        3. Confidence level (deduct for excessive hesitation or fragmented sentences).
        
        Provide a structured output with:
        - A confidence/quality score (0-100)
        - Brief feedback on what was good
        - Brief feedback on what to improve
        
        Format the output exactly like this:
        Score: [number]
        Feedback: [Your feedback text]
        """
    )
    
    chain = prompt | llm
    
    response = chain.invoke({"question": question, "transcript": transcript})
    text_out = response.content
    
    score = 70
    feedback = text_out
    
    for line in text_out.split('\n'):
        if line.startswith('Score:'):
            try:
                score = int(line.split(':')[1].strip())
            except:
                pass
                
    # Simple filler word counting
    fillers = ["uh", "um", "umm", "like", "you know"]
    transcript_lower = transcript.lower()
    found_fillers = [f for f in fillers if f in transcript_lower]
    
    return {
        "score": score,
        "feedback": feedback,
        "filler_words": list(set(found_fillers))
    }
