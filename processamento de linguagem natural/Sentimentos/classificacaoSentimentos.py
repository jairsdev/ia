import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import spacy
from spacy.lang.pt.examples import sentences
import random
from spacy.training import Example
from spacy.tokens import Doc
from preProcessamento import preprocessing

dataTraining = pd.read_csv("base_treinamento.txt", encoding="utf-8")
"""sns.countplot(dataTraining['emocao'], label="Contagem")
plt.show()"""
nlp = spacy.load("pt_core_news_sm")

dataTraining['texto'] = dataTraining['texto'].apply(preprocessing)

dataTrainingFinal = []

for text, emotion in zip(dataTraining['texto'], dataTraining['emocao']):
    if emotion == 'alegria':
        dic = {'ALEGRIA': True, 'MEDO': False}
    else:
        dic = {'ALEGRIA': False, 'MEDO': True}
    
    dataTrainingFinal.append([text, dic.copy()])

model = spacy.blank("pt")
model.add_pipe("textcat")
textcat = model.get_pipe("textcat")
textcat.add_label("MEDO")
textcat.add_label("ALEGRIA")
historic = []
model.begin_training()

for epoch in range(1000):
    random.shuffle(dataTrainingFinal)
    losses = {}
    for batch in spacy.util.minibatch(dataTrainingFinal, 30):
        exampleList = []
        for text, entities in batch:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, {'cats': entities})
            exampleList.append(example)
        model.update(exampleList, losses=losses)
    if epoch % 100 == 0:
        print(losses)
        historic.append(losses)

historicLoss = []
for loss in historic:
    historicLoss.append(loss.get('textcat'))

plt.plot(historicLoss)
plt.title("Progressão do erro")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.show()

model.to_disk("model")