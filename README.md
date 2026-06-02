# 🚀 SkillBridge – AI Resume Analyzer

SkillBridge is an AI-powered Resume vs Job Description matching system that helps users understand how well their resume fits a job role. It uses NLP techniques like TF-IDF, semantic embeddings, and skill extraction to generate an ATS-style compatibility score.

---

## ✨ Features

- 📄 Upload resume (PDF)
- 🧠 AI-based skill extraction
- 📊 Resume–Job matching score
- 🔍 TF-IDF + Cosine Similarity
- 🤖 Semantic similarity using Sentence Transformers
- 🎯 Matched & missing skills detection
- ⚡ FastAPI backend (high performance API)
- 🌐 Simple web frontend (HTML + JavaScript)

---

## 🧠 Tech Stack

Backend: Python, FastAPI, Scikit-learn, Sentence-Transformers, NumPy  
NLP/ML: TF-IDF, Cosine Similarity, Embeddings, Rule-based skill extraction  
Frontend: HTML, CSS, JavaScript (Fetch API)

---

## 📁 Project Structure

SkillBridge/
│
├── api.py                  # FastAPI backend
├── utils/
│   └── analyzer.py        # Core ML pipeline
├── frontend/
│   └── index.html         # UI
├── requirements.txt
└── README.md

---

## ⚙️ How It Works

1. Upload resume (PDF)
2. Paste job description
3. Extract text from resume
4. Extract skills using skill database
5. Compute 3 scores:
   - Jaccard similarity
   - TF-IDF cosine similarity
   - Semantic similarity
6. Combine scores into final weighted score
7. Return result to frontend

---

## 📊 Scoring Formula

Final Score = 0.3 × Jaccard + 0.4 × TF-IDF + 0.3 × Semantic

---

## 🚀 Run Project

Clone repo → install dependencies → run backend → open frontend

pip install -r requirements.txt  
uvicorn api:app --reload  

Open frontend/index.html or use Live Server

---

## 📌 API

GET / → API status

{ "message": "SkillBridge API running" }

POST /analyze → analyze resume

{
  "score_percentage": 51,
  "matched_skills": ["python", "machine learning"],
  "missing_skills": ["aws", "docker"]
}

---

## 🎯 Example

Upload resume → paste job description → get:
- Match score
- Matched skills
- Missing skills
- ATS feedback

---

## 📈 Future Improvements

React frontend, SaaS UI, authentication, database, deployment, AI suggestions

---

## 👨‍💻 Author

Built by Haris – SkillBridge AI System

---

## ⭐ Support

Star the project if you like it
