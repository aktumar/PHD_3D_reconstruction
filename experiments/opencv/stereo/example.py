import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgR = cv.imread('10myleft.png', 0)
imgL = cv.imread('10myright.png', 0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
# stereo = cv.StereoSGBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL, imgR)
cv.imwrite('10my_depth.jpg', disparity)
plt.subplot(1, 3, 1)
plt.imshow(imgL)
plt.subplot(1, 3, 2)
plt.imshow(imgR)
plt.subplot(1, 3, 3)
plt.imshow(disparity, 'gray')
plt.show()
