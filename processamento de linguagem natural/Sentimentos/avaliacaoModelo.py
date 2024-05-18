import spacy
from preProcessamento import preprocessing
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix

dataTest = pd.read_csv("base_teste.txt", encoding="utf-8")
model = spacy.load("model")
predicts = []

for text in dataTest['texto']:
    predict = model(preprocessing(text))
    predicts.append(predict.cats)

catsPredict = []
for predict in predicts:
    if predict['ALEGRIA'] > predict['MEDO']:
        catsPredict.append("alegria")
    else:
        catsPredict.append("medo")

catsTrue = dataTest["emocao"].values
accuracy = accuracy_score(catsTrue, catsPredict)
print(accuracy)