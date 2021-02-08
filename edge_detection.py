import cv2 as cv
import numpy as np

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# gradients are edge like things present in an image, gradients and edges are completely different
# from a mathematical point of view.
gray_image = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image',mat=gray_image)

# laplacian edges
lap = cv.Laplacian(src=gray_image,ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow(winname='lap', mat=lap)

# Sobel method to detect edges
sobel_x = cv.Sobel(src=gray_image, ddepth=cv.CV_64F,dx=1,dy=0)
sobel_y = cv.Sobel(src=gray_image, ddepth=cv.CV_64F,dx=0,dy=1)
combined_sobel = cv.bitwise_or(src1=sobel_x,src2=sobel_y)

cv.imshow(winname='sobel_x', mat=sobel_x)
cv.imshow(winname='sobel_y', mat=sobel_y)
cv.imshow(winname='combined_sobel', mat=combined_sobel)

# canny edge detector
canny = cv.Canny(image=gray_image,threshold1=150,threshold2=175)
cv.imshow(winname='canny', mat=canny)

cv.waitKey(0)
