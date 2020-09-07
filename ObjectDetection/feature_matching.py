# Feature matching extracts defining key features
# from an input image (using ideas from corner,
# edge, and contour detection).
# Then using a distance calculation, finds all
# the matches in a secondary image.
# This means that we are no longer required to
# have an exact copy of the target image!

# 3 Methods:
# - Brute-Force matching with ORB Descriptors
# - Brute-Force matching with SIFT Descriptors
#   and Ratio Test
# - FLANN based Matcher
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

reeses = cv2.imread('../DATA/reeses_puffs.png',0)
cereals = cv2.imread('../DATA/many_cereals.jpg',0)

# Brute-Force matching with ORB Descriptors
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(reeses, None)
kp2, des2 = orb.detectAndCompute(cereals, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches, key=lambda x: x.distance)
reeses_matches = cv2.drawMatches(reeses,kp1,cereals,kp2,matches[:25], None, flags=2)
# display(reeses_matches)

# Brute-Force matching with SIFT Descriptors
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
good = []
# Less distance == better match
# Ratio match1 < 75% match2
for match1, match2 in matches:
    # If match1 distance is less than 75% of match2 distance
    # then descriptor was a good match.
    if match1.distance < 0.75*match2.distance:
        good.append([match1])
sift_matches = cv2.drawMatchesKnn(reeses,kp1,cereals,kp2,good,None,flags=2)
# display(sift_matches)

# FLANN Based Matcher
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
matches_mask = [[0,0] for i in range(len(matches))]
for i,(match1, match2) in enumerate(matches):
    if match1.distance < 0.7*match2.distance:
        matches_mask[i] = [1,0]
draw_params = dict(matchColor=(0,255,0),singlePointColor=(255,0,0),matchesMask=matches_mask,flags=0)
flann_matches = cv2.drawMatchesKnn(reeses, kp1, cereals, kp2, matches, None, **draw_params)
display(flann_matches)