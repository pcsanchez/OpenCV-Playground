# Canny edge detector.
# 1. Apply Gaussian Filter to smooth the image
#    in order to remove noise.
# 2. Find the intensity gradients of the image.
# 3. Apply non-maximum supressions to get rid
#    of spurious response to edge detection.
# 4. Apply double threshold to determine
#    potential edges.
# 5. Track edges by hysterisis.
# For high resolution images where you only
# want general edges, it is usually a good
# idea to apply a custom blur before applying
# the Canny Algorithm.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../DATA/sammy_face.jpg')
blurred_img = cv2.blur(img, ksize=(5,5))
med_val = np.median(img)
# Lower threshold to either 0 or 70% of the median value.
lower = int(max(0,0.7*med_val))
# Upper threshold to either 130% of the median or 255.
upper = int(min(255,1.3*med_val))
edges = cv2.Canny(image=blurred_img, threshold1=lower,threshold2=upper+100)
plt.imshow(edges)
plt.show()