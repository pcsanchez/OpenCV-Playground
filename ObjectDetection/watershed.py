# Any grayscale image can be viewed as a 
# topographic surface where high intensity
# denotes peaks and hills while low intensity
# denotes valleys.
# The watershed algorithm can then fill every
# isolated valleys (local minima) with different
# colored water (labels).

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()

sep_coins = cv2.imread('../DATA/pennies.jpg')

# Manual Segmentation
# Median blur to remove unwanted features
sep_blur = cv2.medianBlur(sep_coins,25)
# Change the Image to Grayscale
gray_sep_blur = cv2.cvtColor(sep_blur, cv2.COLOR_BGR2GRAY)
# Apply Binary Threshold
ret, sep_thresh = cv2.threshold(gray_sep_blur, 160, 255, cv2.THRESH_BINARY_INV)
# display(sep_thresh)
# Find Contours
contours, hierarchy = cv2.findContours(sep_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep_coins, contours, i, (255,0,0),10)
# display(sep_coins)

# Using Watershed
img = cv2.imread('../DATA/pennies.jpg')
img = cv2.medianBlur(img, 35)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# Noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown==255] = 0
markers = cv2.watershed(img, markers)
contours, hierarchy = cv2.findContours(markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep_coins, contours, i, (255,0,0),10)
display(sep_coins)
