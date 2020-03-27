import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

# This is a test, I dont know what this is

y = pickle.load(open("y.pickle","rb"))
X = pickle.load(open("X.pickle","rb"))

#Normalize data
X = X/255.0

# Conbinations
dense_layers = [0,1,2]
layer_sizes = [32,64,128]
conv_layers = [1,2,3]

#Model building
for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "flipped-{}-conv-{}-nodes-{}-dense-{}".format(conv_layer,layer_size,dense_layer,int(time.time()))
            tensorboard = TensorBoard(log_dir="logs\{}".format(NAME))

            model = Sequential()
        
            model.add(Conv2D(layer_size, (3,3), input_shape = X.shape[1:]))
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2,2)))

            for l in range(conv_layer-1):
                model.add(Conv2D(layer_size, (3,3)))
                model.add(Activation("relu"))
                model.add(MaxPooling2D(pool_size=(2,2)))
                
            model.add(Flatten())

            for l in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation('relu'))

            model.add(Dense(1))
            model.add(Activation("sigmoid"))

            model.compile(loss="binary_crossentropy", optimizer="adam", metrics =["accuracy"])
            print()
            print(NAME)
            model.fit(X,y, batch_size = 32, epochs = 15, validation_split=0.3, callbacks = [tensorboard])

# model.save(NAME + ".model")   