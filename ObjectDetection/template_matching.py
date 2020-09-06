# Template matching is the simplest form of 
# object detection.
# It simply scans a larger image for a provided
# template by sliding the template target image
# across the larger image.

import cv2
import numpy as numpy
import matplotlib.pyplot as plt

full = cv2.imread('../DATA/sammy.jpg')
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

face = cv2.imread('../DATA/sammy_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:

    # Create a copy of the image
    full_copy = full.copy()

    method = eval(m)

    # Template matching
    res = cv2.matchTemplate(full_copy, face, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    height, width, channels = face.shape

    bottom_right = (top_left[0] + width, top_left[1]+height)

    cv2.rectangle(full_copy, top_left, bottom_right, (255,0,0), 10)

while True:
    cv2.imshow('face', full_copy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
