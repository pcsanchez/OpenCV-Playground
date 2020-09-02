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