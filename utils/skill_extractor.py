skill_DB = {
    "python": ["python", "py"],
    "java": ["java"],
    "sql": ["sql", "mysql", "postgresql", "sqlite"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl", "neural networks"],
    "nlp": ["nlp", "natural language processing"],
    "tensorflow": ["tensorflow", "tf"],
    "pytorch": ["pytorch", "torch"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "aws": ["aws", "amazon web services"],
    "docker": ["docker", "containerization"],

    "flask": ["flask"],
    "fastapi": ["fastapi"],
    "django": ["django"],

    "scikit-learn": ["scikit-learn", "sklearn"],
    "opencv": ["opencv", "computer vision"],

    "rnn": ["rnn", "recurrent neural network"],
    "lstm": ["lstm", "long short term memory"],
    "gru": ["gru", "gated recurrent unit"],
    "cnn": ["cnn", "convolutional neural network"],
    "transformers": ["transformers", "bert", "gpt"],

    "git": ["git", "github"],
    "linux": ["linux", "ubuntu"],
    "api": ["api", "rest api", "restful api"],

    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],

    "data analysis": ["data analysis", "data analytics"],
    "data visualization": ["data visualization", "matplotlib", "seaborn"],

    "power bi": ["power bi"],
    "tableau": ["tableau"]
}
def extract_skills(text):
    extracted_skills = set()

    text_lower = text.lower()
    tokens = text_lower.split()
    token_set = set(tokens)

    for skill, aliases in skill_DB.items():

        for alias in aliases:

            if " " not in alias:
                if alias in token_set:
                    extracted_skills.add(skill)
                    break

            else:
                if alias in text_lower:
                    extracted_skills.add(skill)
                    break

    return extracted_skills