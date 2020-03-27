import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pickle
import random

CATEGORIES = ["Dog", "Cat"]
DATADIR = os.getcwd()
IMG_SIZE = 85

training_data = []

def create_training_data():
    """Prepares the images, turns them to gray scale and scales down the size of the image"""
    for category in CATEGORIES:
        counter = 0
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        total = len(os.listdir(path))
        print(total)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
            counter = counter + 1
            if counter % 1000 == 0:
                print("Image: ", counter, "; Out of: ", total)
create_training_data()

random.shuffle(training_data)

#Create the array
X = []
y = []
for features , label in training_data:
    X.append(features)
    y.append(label)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = np.array(y)

#Save the array
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

print("All the images are done")