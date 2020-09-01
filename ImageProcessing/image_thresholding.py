# Thresholding is fundamentally a very simple method
# of segmenting an image into different parts.
# Thresholding will convert and image to consist
# of only two values, white or black.
import cv2
import matplotlit.pyplot as plt

img = cv2.imread('/a/fake/path')

# Read an image in grayscale.
img = cv2.imread('/a/fake/path', 0)
plt.imshow(img,cmap='gray')

# Any value below 127 will become a 0 and any value above it will
# become a 1.
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='gray')

img = cv2.imread('/a/fake/path', 0)
plt.imshow(img, cmap='gray')

def show_pic(img):
    fid = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

# Adaptive Threshold.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
show_pic(th2)

blended = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4,gamm=0)
show_pic(blended)