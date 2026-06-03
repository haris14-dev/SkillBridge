from fastapi import FastAPI, UploadFile, File, Form
import tempfile
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

from utils.analyzer import analyze_resume_job
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://skill-bridge-git-main-haris14-devs-projects.vercel.app",
        "https://skill-bridge-two-gold.vercel.app",
        "https://skill-bridge-laf23kdzl-haris14-devs-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SkillBridge API running"}

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await resume.read())
        resume_path = tmp.name

    result = analyze_resume_job(resume_path, job_description)
    return result
