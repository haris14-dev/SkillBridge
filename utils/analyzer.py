from utils.pdf_parser import extract_text_from_pdf
from utils.matching import jaccard, tfidf_similarity, semantic_similarity, final_score
from utils.skill_extractor import extract_skills
from utils.preprocessing import clean_text

def analyze_resume_job(resume_path,job_description):
    resume_text=extract_text_from_pdf(resume_path)
    if resume_text is None:
        print("Failed to extract text from the resume.")
        return None
    cleaned_resume=clean_text(resume_text)  
    cleaned_job_description=clean_text(job_description)

    resume_skills=extract_skills(cleaned_resume)
    job_skills=extract_skills(cleaned_job_description)

    jaccard_score=jaccard(resume_skills,job_skills)
    tfidf_score=tfidf_similarity(cleaned_resume,cleaned_job_description)
    semantic_score=semantic_similarity(cleaned_resume,cleaned_job_description)
    final_score_value=final_score(jaccard_score,tfidf_score,semantic_score)
    score_percentage = round(final_score_value * 100, 2)

    matched_skills=resume_skills.intersection(job_skills)
    missing_skills=job_skills.difference(resume_skills)

    return {
        "jaccard": jaccard_score,
        "tfidf": tfidf_score,
        "semantic": semantic_score,
        "score_percentage": score_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,  
    }