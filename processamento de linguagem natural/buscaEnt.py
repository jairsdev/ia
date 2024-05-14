import bs4 as bs
import spacy
from spacy.lang.pt.examples import sentences
import urllib.request
from spacy.matcher import PhraseMatcher

data = urllib.request.urlopen("https://pt.wikipedia.org/wiki/League_of_Legends")
data = data.read()
dataHtml = bs.BeautifulSoup(data, "lxml")
paragraphs = dataHtml.find_all("p")
content = ''

for paragraph in paragraphs:
    content += paragraph.text

pln = spacy.load("pt_core_news_sm")
text = pln(content)

for token in text.ents:
    print(token.text, token.label_)