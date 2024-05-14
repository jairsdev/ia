import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import PIL.Image
import numpy as np
from keras import utils, models, layers, losses
import pathlib
import PIL
from sklearn.metrics import accuracy_score

dicTrain = pathlib.Path("./dataset/training_set").with_suffix("")
dicValidation = pathlib.Path("./dataset/test_set").with_suffix("")

dicList = []
for classes in dicValidation.iterdir():
    if classes.is_dir():
        for image in classes.iterdir():
            dicList.append(classes.name)
y = []
i = 0
for name in dicList:
    if name == "cachorro":
        y.insert(i, 0)
    else:
        y.insert(i, 1)
    i += 1
"""dataTrainList = list(dataTrain.glob("*/*"))
print(len(dataTrainList))
image = PIL.Image.open(dataTrainList[0])
image.show()"""

dataTrain = utils.image_dataset_from_directory(dicTrain, image_size=(64, 64), batch_size=8)
dataValidation = utils.image_dataset_from_directory(dicValidation, image_size=(64, 64), batch_size=8, shuffle=False)

dataAugmentation = models.Sequential([
    layers.Input((64, 64, 3)),
    layers.RandomRotation(0.1),
    layers.RandomFlip("horizontal"),
    layers.RandomZoom(0.2)
])

model = models.Sequential([
    dataAugmentation,
    layers.Rescaling(1./255),
    layers.Conv2D(16, (3, 3), padding="same", activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(2, activation="softmax")
])
model.compile(optimizer="adam", loss=losses.SparseCategoricalCrossentropy, metrics=["accuracy"])
model.summary()

history = model.fit(dataTrain, validation_data=dataValidation, validation_split=0.2, epochs=20)
predicts = model.predict(dataValidation)
predictsBinary =  np.argmax(predicts, axis=1)
accuracy = accuracy_score(predictsBinary, y)
print(accuracy)