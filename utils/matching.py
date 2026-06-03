from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def jaccard(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if len(union) == 0:
        return 0.0
    return len(intersection) / len(union)


def tfidf_similarity(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    documents = [resume_text, job_description]
    matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(matrix[0], matrix[1])
    return float(similarity[0][0])


#  Disabled semantic model (prevents Render crash)
def semantic_similarity(resume_text, job_description):
    return 0.0


def final_score(jaccard_score, tfidf_score, semantic_score):
    return float(0.5 * jaccard_score + 0.5 * tfidf_score)
