from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import analyze, interview

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend for AI Resume Analyzer and Interview Coach",
    version="1.0.0"
)

# CORS Middleware for Streamlit integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router, prefix="/api/v1")
app.include_router(interview.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API is running"}
