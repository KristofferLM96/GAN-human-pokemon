from PIL import Image
import os

path_flip = "data/pokemon/sketch/temp/"
dirs_flip = os.listdir(path_flip)
flipfolder = path_flip + "/flipped"


try:
    os.mkdir(flipfolder)
except OSError:
    print("Creation of the directory %s failed" % flipfolder)
else:
    print("Successfully created the directory %s " % flipfolder)


def flip():
    number = 1
    for item in dirs_flip:
        if "jpg" in item:
            print("Flipping!", "Number ", number)
            toflip = Image.open(path_flip + '/' + item)
            flipped = toflip.transpose(Image.FLIP_LEFT_RIGHT)
            flipped.save(flipfolder + "/" + str(number) + ".jpg", 'jpeg', quality=100)
            number = number + 1


print(dirs_flip)
flip()
