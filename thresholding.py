import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# grayscale image
gray_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image',mat=gray_image)

# Threholding is binarization of image, in general an image will converted to binary image
# where either color will be 0[black] or 1[white]
# simple thresholding: if value is greater than thresholding value [150], then value will be set to max value or else 0
thresholding, thresh = cv.threshold(src=gray_image,thresh=150, maxval=255,type=cv.THRESH_BINARY)
cv.imshow(winname='Simple threshold', mat=thresh)

# for below type, if value is greater than thresholding value [150], then value will be set to 0 or else 255
thresholding, thresh_inverse = cv.threshold(src=gray_image,thresh=150, maxval=255,type=cv.THRESH_BINARY_INV)
cv.imshow(winname='Inverse Simple threshold', mat=thresh_inverse)

# adapted threshold: here the script itself finds the optimal threshold value
# block size is the kernel size for it to compute the threshold value
adaptive_thresh = cv.adaptiveThreshold(src=gray_image,
                                       maxValue=255,
                                       adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
                                       thresholdType= cv.THRESH_BINARY,
                                       blockSize=11,
                                       C=3)
cv.imshow(winname='Adaptive threshold', mat=adaptive_thresh)

# using gaussian instead of mean for method
adaptive_thresh_gauss = cv.adaptiveThreshold(src=gray_image,
                                       maxValue=255,
                                       adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       thresholdType= cv.THRESH_BINARY,
                                       blockSize=11,
                                       C=3)
cv.imshow(winname='Adaptive threshold Gaussian', mat=adaptive_thresh_gauss)

cv.waitKey(0)