import fitz  # PyMuPDF
import spacy
import re
import os

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a given PDF file."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def clean_text(text: str) -> str:
    """Clean extracted resume text."""
    # Remove extra newlines, special characters
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[^\w\s\.\,\@\-\:\/]', '', text)
    return text.strip()

def extract_entities(text: str) -> dict:
    """Extract key information using NLP and RegEx."""
    doc = nlp(text)
    
    # 1. Extract Emails
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    
    # 2. Extract Phone numbers (basic regex)
    phones = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    
    # 3. Extract standard Skills (basic dictionary approach)
    # We will expand this with a more comprehensive list later.
    COMMON_SKILLS = ["python", "java", "c++", "sql", "pandas", "numpy", "aws", "docker", 
                     "kubernetes", "machine learning", "nlp", "fastapi", "react", "html", 
                     "css", "javascript", "langchain", "pytorch", "tensorflow", "git", 
                     "github", "flask", "django"]
    
    extracted_skills = []
    text_lower = text.lower()
    for skill in COMMON_SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
            extracted_skills.append(skill.title() if len(skill)>3 else skill.upper())
            
    return {
        "email": emails[0] if emails else None,
        "phone": phones[0] if phones else None,
        "skills": list(set(extracted_skills))
    }

def parse_resume(pdf_path: str) -> dict:
    """Main pipeline for parsing a resume PDF."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
        
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    entities = extract_entities(cleaned_text)
    
    return {
        "raw_text": cleaned_text,
        "parsed_data": entities
    }
