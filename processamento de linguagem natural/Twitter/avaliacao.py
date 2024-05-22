import spacy
from preprocessamento import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

dataTest = pd.read_csv("Test.csv", delimiter=";")
dataTest = dataTest.sample(frac=1)
dataTest = dataTest.head(500)
model = spacy.load("model")

predicts = []
for text in dataTest["tweet_text"]:
    text = preprocessing(text)
    predict = model(text).cats
    predicts.append(predict)

catPredict = []
for predict in predicts:
    if predict['ALEGRIA'] > predict['TRISTEZA']:
        catPredict.append(1)
    else:
        catPredict.append(0)

catTrue = dataTest["sentiment"].values

print(accuracy_score(catTrue, catPredict))