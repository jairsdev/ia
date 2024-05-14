import bs4 as bs
import spacy
import nltk
from spacy.lang.pt.examples import sentences
import urllib.request
from spacy.matcher import PhraseMatcher
import IPython

class HTML:
    def __init__(self, text):
        self.text = text
    
    def _repr_html_(self):
        return f"<h1>{self.text.upper()}</h1>"

data = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Club_de_Regatas_Vasco_da_Gama")
data = data.read()
dataHtml = bs.BeautifulSoup(data, "lxml")
paragraphs = dataHtml.find_all("p")
content = ''
for paragraph in paragraphs:
    content += paragraph.text
content = content.lower()

pln = spacy.load("pt_core_news_sm")
string = 'dinamite'
tokenSearch = pln(string)
matcher = PhraseMatcher(pln.vocab)
matcher.add('SEARCH', None, tokenSearch)

doc = pln(content)
matches = matcher(doc)
"""print(matches)
print(doc[2630-5:2631+5])"""
numeroPalavras = 50

results = ''
for match in matches:
    start = match[1] - numeroPalavras
    if start < 0:
        start = 0
    results += "..."
    results += doc[start:match[2]+numeroPalavras].text
    results += "..."
    results += "\n\n"
text = f"""{string.upper()}

Resultados encontrados: {len(matches)}

{results}
"""
print(text)

