from fastapi import FastAPI, UploadFile, File, Form
import tempfile
from utils.analyzer import analyze_resume_job
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(    #for frontend and backend to communicate with each other without any CORS issues, we can add the CORSMiddleware to our FastAPI application. This middleware allows us to specify which origins are allowed to access our API, as well as which HTTP methods and headers are permitted. In this case, we are allowing all origins, credentials, methods, and headers for simplicity, but in a production environment, you may want to restrict these settings for better security.
    CORSMiddleware,
    allow_origins=["https://skill-bridge-git-main-haris14-devs-projects.vercel.app/",
                  https://skill-bridge-two-gold.vercel.app/,
    https://skill-bridge-laf23kdzl-haris14-devs-projects.vercel.app/],
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
