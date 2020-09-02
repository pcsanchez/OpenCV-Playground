# An image gradient is a directional change in the
# intensity or color in an image.
# Gradients can be calculated in a specific direction.
# The operator uses two 3x3 kernels which are convolved
# with the original image to calculate approximations of
# the derivatives - one for horizontal changes, and one
# for vertical.

# +1 0 -1         +1 +2 +1
# +2 0 -2 * A and  0  0  0 * A
# +1 0 -1         -1 -2 -1

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

img = cv2.imread('/a/fake/path',0)
display_img(img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display_img(sobelx)

sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
display_img(sobely)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
display_img(laplacian)

blended = cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)
display_img(blended)

kernel = np.ones((4,4),np.uint8)
gradient = cv2.morphologyEx(blended, cv2.MOPRH_GRADIENT,kernel)
display_img(gradient)