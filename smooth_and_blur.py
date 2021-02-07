import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# Generally smoothing is applied when image has lot of noise
# and this noise may be caused by camera sensors or problems in lighting
# when image was taken. Smoothing or reduce some of the noise
# by applying blurring method

# averaging for blur
# here the color window over specific portion of image
# this window will compute the pixel intensity of the middle pixel
# of true center as the average of surrounding pixel intensities

average_blur = cv.blur(src=img, ksize=(3,3))
cv.imshow(winname='average_blur', mat=average_blur)

# higher the kernel size, more blur will be the image
average_blur = cv.blur(src=img, ksize=(7,7))
cv.imshow(winname='average_blur_high_blur', mat=average_blur)

# Gaussian blur: It is similar to averaging, however instead of computing
# the average of all surrounding pixel intensities, each surrounding pixel
# given a particular weight, the average of products of those weights gives
# the pixel intensity of the middle
# sigmaX is the standard deviation along x-axis
gauss_blur = cv.GaussianBlur(src=img, ksize=(3,3), sigmaX=0)
cv.imshow(winname='gauss_blur', mat=gauss_blur)

# Median Blur: This is similar to averaging, however instead of averaging,
# here the median value of surrounding pixel intensities is taken for
# the middle pixel intensity
median_blur = cv.medianBlur(src=img, ksize=3)
cv.imshow(winname='median_blur', mat=median_blur)

cv.waitKey(0)