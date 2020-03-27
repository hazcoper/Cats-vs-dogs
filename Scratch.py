from PIL import Image
import os
print("heklo")
exit()
print(os.getcwd())
def flip_image(img, number):
    """Receives the number of the image and the new number to save the flipped image"""
    img = Image.open(img)
    img.transpose(Image.FLIP_LEFT_RIGHT).save(cats + "/" + str(number)+ ".jpg")

cats = "Dog"
total = len(os.listdir(cats))
counter = 12499
for cat in range(total):
    counter = counter + 1
    try:
        flip_image(cats + "/" + str(cat)+".jpg", counter)
    except:
        print("image failed: ", cat)