import spacy
import pandas as pd
from spacy.lang.pt.examples import sentences
from preprocessamento import preprocessing
from spacy.util import minibatch
from spacy.training import Example
import random

dataTraining = pd.read_csv("Train50.csv", delimiter=";")
dataTraining = dataTraining.sample(frac=1)
dataTraining = dataTraining.head(1000)

dataTraining["tweet_text"] = dataTraining["tweet_text"].apply(preprocessing)
dataTrainingFinal = []

for text, sentiment in zip(dataTraining["tweet_text"], dataTraining["sentiment"]):
    if (sentiment == 1):
        dic = {"ALEGRIA": True, "TRISTEZA": False}
    else:
        dic = {"ALEGRIA": False, "TRISTEZA": True}
    dataTrainingFinal.append([text, dic.copy()])


model = spacy.blank("pt")
model.add_pipe("textcat")
textcat = model.get_pipe("textcat")
textcat.add_label("ALEGRIA")
textcat.add_label("TRISTEZA")

model.begin_training()

historic = []
nlp = spacy.load("pt_core_news_sm")
for epoch in range(1000):
    random.shuffle(dataTrainingFinal)
    batches = minibatch(dataTrainingFinal, 80)
    losses = {}
    for batch in batches:
        exampleList = []
        for text, sentiment in batch:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, {"cats": sentiment})
            exampleList.append(example)
        model.update(exampleList, losses=losses)
    if epoch % 100 == 0:
        print(losses)
        historic.append(losses)
    
print(historic)
model.to_disk("model")
