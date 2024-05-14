import bs4 as bs
import nltk
import spacy
from spacy.lang.pt.examples import sentences 

nlp = spacy.load("pt_core_news_sm")
text = nlp('Jair é muito bonito')

nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()

for token in text:
    print(token.text, token.pos_, token.lemma_, stemmer.stem(token.text))
