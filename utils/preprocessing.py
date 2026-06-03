import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def get_stopwords():
    try:
        return set(stopwords.words('english'))
    except LookupError:
        nltk.download('stopwords')
        return set(stopwords.words('english'))

stop_words = get_stopwords()
lemmatizer = WordNetLemmatizer()

def to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return re.sub(r'[^\w\s]','',text)  #first argument is regex ^ means find everything that is not w(A_Z a-z 0-9) or s(space) and second argument is empty string which means replace it with nothing
   
def tokenize(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

def lemmatize(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

def clean_text(text):
    text=to_lowercase(text)
    text=remove_punctuation(text)
    tokens=tokenize(text)
    tokens=remove_stopwords(tokens)
    tokens=lemmatize(tokens)    
    return ' '.join(tokens)
