from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def jaccard(set1,set2):
      intersection=set1.intersection(set2)
      union=set1.union(set2)
      if len(union)==0:          #to avoid zero division error when both sets are empty, we can define the Jaccard similarity as 0 
            return 0.0
      return len(intersection)/len(union)   

def tfidf_similarity(resume_text,job_description):
      vectorizer=TfidfVectorizer()
      documents=[resume_text,job_description]
      matrix=vectorizer.fit_transform(documents)   #matrix now becomes a sparse matrix where fit means it learns the vocabulary from the documents and transform means it transforms the documents into a matrix of TF-IDF features. The resulting matrix will have two rows (one for the resume and one for the job description) and columns corresponding to the unique terms in both documents. Each entry in the matrix represents the TF-IDF score of a term in a document.
      similarity=cosine_similarity(matrix[0],matrix[1])
      return float(similarity[0][0])

def semantic_similarity(resume_text,job_description):
      embeddings=model.encode([resume_text,job_description])
      similarity=cosine_similarity([embeddings[0]],[embeddings[1]])
      return float(similarity[0][0])

def final_score(jaccard_score,tfidf_score,semantic_score):
      return float(0.3*jaccard_score + 0.4*tfidf_score + 0.3*semantic_score)










