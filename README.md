# 🚀 SkillBridge – AI Resume Analyzer

SkillBridge is an AI-powered Resume vs Job Description matching system that helps candidates understand how well their resume fits a job role. It uses NLP techniques like TF-IDF, semantic embeddings, and skill extraction to generate an ATS-style compatibility score.

---

## ✨ Features

- 📄 Upload resume (PDF)
- 🧠 AI-based skill extraction
- 📊 Resume–Job matching score
- 🔍 TF-IDF + Cosine Similarity
- 🤖 Semantic similarity using Sentence Transformers
- 🎯 Matched & missing skills detection
- ⚡ FastAPI backend (high performance API)
- 🌐 Simple web frontend (HTML + JS)

---

## 🧠 Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- Sentence-Transformers
- NumPy

### NLP / ML
- TF-IDF Vectorization
- Cosine Similarity
- Embedding-based semantic similarity
- Rule-based skill extraction

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📁 Project Structure

SkillBridge/
│
├── api.py                  # FastAPI backend
├── utils/
│   └── analyzer.py        # Core ML pipeline
│
├── frontend/
│   └── index.html         # UI (resume upload + results)
│
├── requirements.txt
└── README.md

---

## ⚙️ How It Works

1. User uploads a **resume (PDF)**
2. Job description is pasted in the UI
3. Backend extracts text from resume
4. Skills are extracted using a predefined skill database
5. Three similarity scores are computed:
   - Jaccard Similarity
   - TF-IDF Cosine Similarity
   - Semantic Similarity (Embeddings)
6. Final weighted score is calculated
7. Results are returned to frontend

---

## 📊 Scoring Formula

Final Score =
0.3 × Jaccard Similarity +
0.4 × TF-IDF Similarity +
0.3 × Semantic Similarity

---

## 🚀 Run the Project

### 1. Clone repository
```bash
git clone https://github.com/your-username/SkillBridge.git
cd SkillBridge
2. Install dependencies
pip install -r requirements.txt
3. Run backend server
uvicorn api:app --reload
4. Open frontend

Open:
frontend/index.html

OR use Live Server (VS Code) for best experience.

📌 API Endpoints
GET /

Returns API status

{ "message": "SkillBridge API running" }
POST /analyze

Form Data:

resume (PDF file)
job_description (string)

Response:

{
  "score_percentage": 51,
  "matched_skills": ["python", "machine learning"],
  "missing_skills": ["aws", "docker"]
}
🎯 Example Use Case
Upload resume
Paste job description
Get:
Match score
Matched skills
Missing skills
ATS-style feedback
📈 Future Improvements
React frontend (modern SaaS UI)
Skill weighting system (ATS-level scoring)
AI resume improvement suggestions
User authentication
Database for storing results
Cloud deployment (AWS / Render / Vercel)
👨‍💻 Author

Built by Haris
Project: SkillBridge – AI Resume Intelligence System

⭐ Support

If you like this project, consider giving it a star ⭐


---

If you want next upgrade, I can help you turn this into a:

🚀 **real SaaS portfolio project (React + dashboard + login + deployment)**
