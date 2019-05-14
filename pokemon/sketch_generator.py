import imageio
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

# Load image(s)
img = ""
start_img = imageio.imread(img)


# Function for applying greyscaling to an image.
def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


gray_img = grayscale(start_img)  # Applying grescaling to image.
inverted_img = 255-gray_img  # Inverting image
# Blurring image. As sigma increases, the blur increases.
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img, sigma=5)


# The color dodge divides the bottom layer by the inverted top layer.
# This lightens the bottom layer depending on the value of the top layer.
# The blurred image highlights the boldest edges.
def dodge(front, back):
    result = front*255/(255-back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype("uint8")


final_img = dodge(blur_img, gray_img)

# Plotting and saving the image.
plt.imshow(final_img, cmap="gray")
plt.imsave("img2.png", final_img, cmap="gray", vmin=0, vmax=255)
