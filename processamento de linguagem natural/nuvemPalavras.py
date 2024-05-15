from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import bs4 as bs
import urllib.request
import spacy
from spacy.lang.pt.examples import sentences
from spacy.lang.pt.stop_words import STOP_WORDS

data = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Liverpool_Football_Club")
data = data.read()
dataHtml = bs.BeautifulSoup(data, "lxml")
paragraphs = dataHtml.find_all("p")
content  = ""
for paragraph in paragraphs:
    content += paragraph.text

content = content.lower()

pln = spacy.load("pt_core_news_sm")
doc = pln(content)
docNoStopWords = ""
for token in doc:
    if not token.is_stop:
        docNoStopWords += token.text
        docNoStopWords += " "

colorMap = ListedColormap(["orange", "green", "red", "magenta"])
cloud = WordCloud(background_color="white", max_words=100, colormap=colorMap)
cloud = cloud.generate(docNoStopWords)
plt.figure(figsize=(15, 15))
plt.imshow(cloud)
plt.axis('off')
plt.show()

