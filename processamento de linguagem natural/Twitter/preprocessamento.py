import string
from spacy.lang.pt.examples import sentences
from spacy.lang.pt.stop_words import STOP_WORDS
import spacy

def preprocessing(text):
    nlp = spacy.load("pt_core_news_sm")
    stopWords = STOP_WORDS
    punctuation = string.punctuation

    text = text.lower()
    textLemma = []
    doc = nlp(text)

    for token in doc:
        textLemma.append(token.lemma_)
    
    textProcessing = [word for word in textLemma if word not in stopWords and word not in punctuation and "@" not in word]
    textProcessing = ' '.join(word for word in textProcessing if not word.isdigit())

    return textProcessing
    
    
    
