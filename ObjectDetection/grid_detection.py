# Cameras can create a distortion in an image
# such as radial distortion and tangential
# distortion.
# A good way to account for these distortions
# is to have a recognizable pattern attached
# to the object being tracked.
# Grid patterns are often used to calibrate
# cameras and track motion.
import cv2
import matplotlib.pyplot as plt

flat_chess = cv2.imread('../DATA/flat_chessboard.png')
found, corners = cv2.findChessboardCorners(flat_chess, (7,7))
cv2.drawChessboardCorners(flat_chess, (7,7), corners, found)
plt.imshow(flat_chess)
plt.show()

dots = cv2.imread('../DATA/dot_grid.png')
found, corners = cv2.findCirclesGrid(dots, (10,10), cv2.CALIB_CB_SYMMETRIC_GRID)
cv2.drawChessboardCorners(dots, (10,10), corners, found)
plt.imshow(dots)
plt.show()