# A contour is simply a curve joining all
# the continuous points along a boundary.
# They are useful for shape analysis and
# recognition.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../DATA/internal_external.png', 0)
contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
external_contours = np.zeros(img.shape)
for i in range(len(contours)):

    # External contours
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(external_contours, contours, i, 255, -1)

plt.imshow(external_contours, cmap='gray')
plt.show()

internal_contours = np.zeros(img.shape)
for i in range(len(contours)):

    # Internal contours
    if hierarchy[0][i][3] != -1:
        cv2.drawContours(internal_contours, contours, i, 255, -1)

plt.imshow(internal_contours, cmap='gray')
plt.show()