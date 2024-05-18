import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
import string
def preprocessing(text):
    nlp = spacy.load("pt_core_news_sm")
    stopWords = STOP_WORDS
    punctuation = string.punctuation
    text = text.lower()
    text = nlp(text)
    textPreList = []
    for token in text:
        textPreList.append(token.lemma_)
    textPosList = [word for word in textPreList if word not in stopWords and word not in punctuation]
    textPos = ' '.join(str(element) for element in textPosList if not element.isdigit())

    return textPos