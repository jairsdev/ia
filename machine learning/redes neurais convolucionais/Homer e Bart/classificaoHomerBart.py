import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import PIL.Image
import numpy as np
from keras import utils, models, layers, losses
import pathlib
import PIL
from sklearn.metrics import accuracy_score

dataTrainDic= pathlib.Path("./training_set").with_suffix('')
dataValidationDic = pathlib.Path("./test_set").with_suffix('')
lenTraining = len(list(dataTrainDic.glob('*/*')))
#print(list(data_dir.glob("*/*")))
#print(lenTraining)
yClasses = []
for classe in dataValidationDic.iterdir():
    if classe.is_dir():
        for imagem in classe.iterdir():
            yClasses.append(classe.name)
y = []
i = 0

for nome in yClasses:
    if (nome == "bart"):
        y.insert(i, 0)
    else:
        y.insert(i, 1)
    i += 1
"""bart = list(dataTrainDic.glob("bart/*"))
image = PIL.Image.open(str(bart[8]))
image.show()"""

dataTrain = utils.image_dataset_from_directory(dataTrainDic, image_size=(64, 64), batch_size=8)
dataValidation = utils.image_dataset_from_directory(dataValidationDic, image_size=(64, 64), batch_size=8, shuffle=False)

dataAugmentation = models.Sequential([
    layers.RandomRotation(0.1),
    layers.RandomFlip("horizontal", input_shape=(64, 64, 3)),
    layers.RandomZoom(0.2)
])
model = models.Sequential([
    dataAugmentation,
    layers.Rescaling(1./255, input_shape=(64, 64, 3)),
    layers.Conv2D(16, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(32, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(2, activation="softmax")
])

model.compile(optimizer="adam", loss=losses.SparseCategoricalCrossentropy, metrics=["accuracy"])
model.summary()

model.fit(dataTrain, validation_data=dataValidation, validation_split=0.2, epochs=100)
predicts = model.predict(dataValidation)
predicts2 = np.argmax(predicts, axis=1)
"""print(predicts2)
print(y)"""

accuracyTest = accuracy_score(predicts2, y)
print(accuracyTest)