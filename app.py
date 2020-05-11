# inspired by: https://medium.com/swlh/tic-tac-toe-and-deep-neural-networks-ea600bc53f51

from gamelib import initBoard, checkWinner, printBoard, stats, simulateGame
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils.np_utils import to_categorical
from keras.backend import reshape
import numpy as np

def createData(count=10000):
    X = []
    Y = []
    games = [simulateGame() for _ in range(count)]
    
    for game in games:
        X.append(game[0])
        Y.append(game[1])

    return (X, Y)

def splitData(data, train=0.8):
    trainCount = int(len(data) * train)
    X = np.array(data[0]).reshape((-1,9))
    Y = to_categorical(data[1])

    return (X[:trainCount], X[trainCount:], Y[:trainCount], Y[trainCount:])

def getModel():
    model = Sequential()
    model.add(Dense(200, activation='relu', input_shape=(9, )))
    model.add(Dropout(0.2))
    model.add(Dense(125, activation='relu'))
    model.add(Dense(75, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])

    return model

df = createData(10)
X_train, X_test, Y_train, Y_test = splitData(df)

model = getModel()
log = model.fit(X_train, Y_train, validation_data=(X_test, Y_test)
, epochs=100, batch_size=100)

