import os
from skimage.util import random_noise
import cv2
import numpy as np



def add_noise(img, number):
    """Receives an image adds noise flips and saves as a new image with the right number"""
    # Load the image
    img = cv2.imread(img)

    #Flip Image
    img = cv2.flip(img, 1)

    # Add salt-and-pepper noise to the image.
    noise_img = random_noise(img, mode='s&p',amount=0.3)
    
    # The above function returns a floating-point image
    # on the range [0, 1], thus we changed it to 'uint8'
    # and from [0,255]
    noise_img = np.array(255*noise_img, dtype = 'uint8')
    
    #Save image
    cv2.imwrite(cats + "/" + str(number) + ".jpg", noise_img)

cats = "Dog"
total = len(os.listdir(cats))
counter = 12499
for cat in range(total):
    counter = counter + 1
    try:
        add_noise(cats + "/" + str(cat)+".jpg", counter)
        break
    except:
        print("image failed: ", cat)
