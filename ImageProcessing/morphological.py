# Morphological operators are sets of kernels
# that can achieve a variety of effects, such
# as reducing noise.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255))
    return blank_img

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

img = load_img()
display_img(img)

# Erotion
kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img,kernel,iterations=4)
display_img(result)

# Opening is useful to get rid of noise.
# It is erotion followed by dilation.
img = load_img()
white_noise = np.random.randint(low=0,high=2,size=(600,600))
white_noise = white_noise * 255
white_img = white_noise + img

opening = cv2.morphologyEx(noise_img,cv2.MORPH_OPEN,kernel)
display_img(opening)

# Closing is the opposite of opening.
# Dialtion followed by erosion.
img = load_img()
black_noise = np.random.randint(low=0,high=2,size=(600,600))
black_noise = black_noise * -255
black_noise_img = img + black_noise

black_noise_img[black_noise_img == -255] = 0
display_img(black_noise_img)

closing = cv2.morphologyEx(black_noise_img,cv2.MORPH_CLOSE,kernel)
display_img(closing)

img = load_img()
display_img(img)

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)