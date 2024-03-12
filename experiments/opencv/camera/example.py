# import numpy as np
# import cv2 as cv
# import glob
#
# # termination criteria
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# objp = np.zeros((5 * 5, 3), np.float32)
# objp[:, :2] = np.mgrid[0:5, 0:5].T.reshape(-1, 2)
# # Arrays to store object points and image points from all the images.
# objpoints = []  # 3d point in real world space
# imgpoints = []  # 2d points in image plane.
# images = glob.glob('*.jpg')
# for fname in images:
#     img = cv.imread(fname)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # Find the chess board corners
#     ret, corners = cv.findChessboardCorners(gray, (5, 5), None)
#     # If found, add object points, image points (after refining them)
#
#     print(ret)
#
#     if ret == True:
#         objpoints.append(objp)
#         corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#         imgpoints.append(corners2)
#         # Draw and display the corners
#         cv.drawChessboardCorners(img, (5, 5), corners2, ret)
#         # cv.imshow('img', img)
#         # cv.waitKey(500)
#
# ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
#
# # np.savez('B.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
#
# cv.destroyAllWindows()

#############################################################################################

# img = cv.imread('left16.jpg')
# h, w = img.shape[:2]
# newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
#
# # undistort
# dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('left16_calibresult.png', dst)
#
# # undistort
# mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
# dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('left16_calibresult.png', dst)

#############################################################################################

import numpy as np
import cv2 as cv
import glob

# Load previously saved data
with np.load('B.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]

axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)
def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())

    imgpts_0 = tuple(imgpts[0].ravel())
    imgpts_1 = tuple(imgpts[1].ravel())
    imgpts_2 = tuple(imgpts[2].ravel())

    corner = tuple(int(x) for x in corner)
    imgpts_0 = tuple(int(x) for x in imgpts_0)
    imgpts_1 = tuple(int(x) for x in imgpts_1)
    imgpts_2 = tuple(int(x) for x in imgpts_2)

    img = cv.line(img, corner, imgpts_0, (255, 0, 0), 5)
    img = cv.line(img, corner, imgpts_1, (0, 255, 0), 5)
    img = cv.line(img, corner, imgpts_2, (0, 0, 255), 5)
    return img


# axis = np.float32([[0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0],
#                    [0, 0, -3], [0, 3, -3], [3, 3, -3], [3, 0, -3]])
# def draw(img, corners, imgpts):
#     imgpts = np.int32(imgpts).reshape(-1, 2)
#     # draw ground floor in green
#     img = cv.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)
#     # draw pillars in blue color
#     for i, j in zip(range(4), range(4, 8)):
#         img = cv.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)
#     # draw top layer in red color
#     img = cv.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)
#     return img


criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((5 * 5, 3), np.float32)
objp[:, :2] = np.mgrid[0:5, 0:5].T.reshape(-1, 2)

for fname in glob.glob('left*.jpg'):
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (5, 5), None)
    if ret == True:
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        # Find the rotation and translation vectors.
        ret, rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)
        # project 3D points to image plane
        imgpts, jac = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)
        img = draw(img, corners2, imgpts)
        cv.imshow('img', img)
        k = cv.waitKey(0) & 0xFF
        if k == ord('s'):
            cv.imwrite(fname[:6] + '.png', img)
cv.destroyAllWindows()
