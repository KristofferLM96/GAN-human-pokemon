from PIL import Image
import os

path_resize = "data/pokemon/sketch/temp/"
dirs_resize = os.listdir(path_resize)
resizefolder = path_resize + "/resized"


try:
    os.mkdir(resizefolder)
except OSError:
    print("Creation of the directory %s failed" % resizefolder)
else:
    print("Successfully created the directory %s " % resizefolder)


def resize():
    number = 1
    for item in dirs_resize:
        if "jpg" in item:
            print("Resizing!", "Number ", number)
            im = Image.open(path_resize + '/' + item)
            f, e = os.path.splitext(path_resize+item)
            imResize = im.resize((200, 200), Image.ANTIALIAS)
            imResize.save(resizefolder + "/" + str(number) + ".jpg", 'jpeg', quality=100)
            number = number + 1


print(dirs_resize)
resize()
