import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('personagens.csv', encoding='utf-8')
"""print(dataset.shape)
print(dataset.head())
print(dataset.tail())
datasetNew = dataset.drop('classe', axis=1)
sns.countplot(x="classe", data=dataset)
sns.heatmap(datasetNew.corr(), annot=True)
plt.show()"""

X = dataset.iloc[:, 0:6].values
#print(X)

y = dataset.iloc[:, 6].values
#print(y)
y = (y == 'Bart')
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2)
print(XTrain)
print(yTrain)
#6 -> 4 -> 4 -> 4 -> 1
neuralNetwork = tf.keras.models.Sequential()
neuralNetwork.add(tf.keras.layers.Dense(units=4, activation='relu', input_shape=(6,)))
neuralNetwork.add(tf.keras.layers.Dense(units=4, activation='relu'))
neuralNetwork.add(tf.keras.layers.Dense(units=4, activation='relu'))
neuralNetwork.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

print(neuralNetwork.summary())
neuralNetwork.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

history = neuralNetwork.fit(XTrain, yTrain, epochs=50, validation_split=0.1)