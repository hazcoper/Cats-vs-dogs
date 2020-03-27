import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

CATEGORIES = ["Dog", "Cat"]

def prepare(filepath):
    IMG_SIZE = 85
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
    plt.imshow(new_array, cmap="gray")
    plt.show()
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


filepath = "Cat.jpg"

model = tf.keras.models.load_model("Cats-vs-dogs-cnn-64x2-1585080278.model")

preped_image = prepare(filepath)

pred = model.predict([preped_image])
print(CATEGORIES[int(pred[0][0])])
