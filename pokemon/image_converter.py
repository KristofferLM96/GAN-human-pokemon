from PIL import Image
import os
import random
import string

# Path should be the folder containing the pictures
path = "data/pokemon/sketch/temp/"

dirs = os.listdir(path)
print(path)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# If png files is detected, they will be converted into jpg.
def tojpg():
    number = 1
    for item in dirs:
        if "png" in item:
            print("PNG to JPG convert on ", path + '/' + item)
            im = Image.open(path + '/' + item)
            conim = im.convert('RGB')
            conim.save(path + '/' + str(number) + randomString() + ".jpg", 'jpeg', quality=100)
            if os.path.exists(path + '/' + item):
                os.remove(path + '/' + item)
            else:
                print("The file does not exist")
            number = number + 1


tojpg()
