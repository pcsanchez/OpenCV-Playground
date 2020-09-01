import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read images.
img1 = cv2.imread("/path/to/image")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("/path/to/image")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.imshow(img2)

img1.shape
img2.shape

# Blending images of the same size.
img1 = cv2.resize(img1, (1200, 1200))
img2 = cv2.resize(img2, (1200, 1200))

# Alpha and Beta values determine which image is more predominant.
# addWeighted only works on images of the same size.
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2,beta=0.5,gamma=0)

# Overlay a small image on top of a large image (no blending).
# Numpy reassignment operation.
img1 = cv2.imread("/path/to/image")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("/path/to/image")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600, 600))

large_img = img1
small_img = img2

x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

small_img.shape

large_img[y_offset:y_end, x_offset:x_end] = small_img
plt.imshow(large_img)

# Blend together images of different sizes.
img1 = cv2.imread("/path/to/image")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("/path/to/image")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600, 600))

# Figure out the dimensions of img1.
img1.shape

x_offset = 934 - 600
y_offset = 1401 - 600

rows, cols, channels = img2.shape

roi = img1[y_offset:1401, x_offset:943]

img2gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

mask_inv = cv2.bitwise_not(img2gray)

white_background = np.full(img2.shape, 255, dtype=np.uint8)

bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)

fg = cv2.bitwise_or(img2, img2, mask=mask_inv)

plt.imshow(fg)

final_roi = cv2.bitwise_or(roi,fg)

plt.imshow(final_roi)

large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
plt.imshow(large_img)