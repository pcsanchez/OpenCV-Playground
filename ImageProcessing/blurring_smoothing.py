# A common operation of image processing is blurring
# or smoothing of an image.
# Smoothing an image can help get rid of noise, or
# help an application focus on general details.
# There are many methods of blurring and smoothing.

# Blurring and smoothing is combined with edge
# detection.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img(path):
    img = cv2.imread(path).astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)

i = load_img('/path')
display_img(i)

# Gamma correction
# This can be applied to an image to make it
# appear brighter or darker.
# Chossing values < than 1 makes the image lighter
# while choosing values > 2 make the image darker.
gamma = 1/4
result np.power(i, gamma)
display_img(result)

# Applying a low pass filter to blurr an image.
img = load_img('path')
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10,600) fontFace=font,fontScale=10, color(255,0,0), thickness=4)
display_img(img)

kernel = np.ones(shape=(5,5), dtype=np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
display_img(dst)

# Smooth an image based off averaging.
blurred = cv2.blur(img, ksize=(5,5))
display_img(blurred)

# Gaussian blur.
blurred_img = cv2.GaussianBlur(img, (5,5), 10)
display_img(blurred_img)

# Median blur.
median_result = cv2.medianBlur(img, 5)
display_img(median_result)

# Bilateral filter
blur = cv2.bilateralFilter(img,9,75,75)
display_img(blur)