# A histogram is a visual representation of
# the distribution of a continuous feature.
# For images, we can display the frequency
# of values for colors.

import cv2
import numpy as np
import matplotlib.pyplot as plt

dark_horse = cv2.imread('path')
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('path')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('path')
show_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)

hist_values = cv2.calcHist([blue_bricks],channels=[0],mask=None,histSize=[256],ranges=[0,256])

img = blue_bricks
color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
    plt.ylim([0,500000])

plt.title('Histogram for blue bricks')

# Applying a mask to an image and creating a histogram.
img = rainbow
mask = np.zeros(img,shape[:2], np.uint8)
mask[300:400,100:400] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)
show_masked_img = cv2.bitwise_and(show_rainbow, show_rainbow, mask=mask)
hist_mask_values_red = cv2.calcHist([rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0,256])
plt.plot(hist_mask_values_red)
plt.title('RED HISTOGRAM FOR MASKED RAINBOW')

# Historgram Equalization.
gorilla = cv2.imread('DATA/gorilla.jpg', 0)
def display(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)

display(gorilla, cmap='gray')
hist_values = cv2.calcHist([gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values)
eq_gorilla = cv2.equalizeHist(gorilla)
display(eq_gorilla, cmap=gray)
hist_values = cv2.calcHist([eq_gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values)

color_gorilla = cv2.imread('DATA/gorilla.jpg')
hsv = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2HSV)
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
eq_color_gorilla = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
display(eq_color_gorilla)