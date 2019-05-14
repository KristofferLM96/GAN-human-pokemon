import cv2
import glob
import os

images = [cv2.imread(file) for file in glob.glob("dataset/human/original/*.jpg")]
filenames = []
for root, dirs, files in os.walk("dataset/human/original/"):
    for filename in files:
        filenames.append(filename)
index = 0
for img in images:
    # reading the image
    # img = cv2.imread('dataset/human/original/24729177_1.jpg', 1)
    # converting the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # inverting the image
    img_invert = cv2.bitwise_not(img_gray)
    # blurring or smoothing the inverted image with the kernel size (10,10)
    img_blur = cv2.blur(img_invert, (10, 10))

    """The Dodge blend function divides the bottom layer by the inverted top layer. 
    This lightens the bottom layer depending on the value of the top layer. 
    We have the blurred image, which highlights the boldest edges."""


    def dodgeV2(image, mask):
        return cv2.divide(image, 255 - mask, scale=256)


    final_img = dodgeV2(img_gray, img_blur)

    # displaying the sketch image
    # cv2.imshow('24729177_1.jpg', final_img)
    cv2.imwrite('dataset/human/sketch/'+filenames[index], final_img)
    index += 1
    cv2.destroyAllWindows()
