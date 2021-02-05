import cv2 as cv
import numpy as np

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# creation of blank image, here datatype 'uint8' image type
# height = 600, width = 400, number of color channels = 3
blank_image = np.zeros(shape=img.shape,dtype='uint8')
# cv.imshow(winname='blank_image', mat=blank_image)

# contours are boundaries of objects, the line or curve that joins continous points along the boundary of object
# mathematically they are not same as edges
# contours are useful in object detection and recognition, shape analysis

# converting color to grayscale
gray_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image', mat=gray_image)

#  blur an image, can be used to blur some parts or noise
# to increase the blur, increase the kernel size
blur_image = cv.GaussianBlur(src=img, ksize=(7,7), sigmaX=cv.BORDER_DEFAULT)
cv.imshow(winname='blur_image', mat=blur_image)

# edge detection using canny
canny_image = cv.Canny(image=img, threshold1=125, threshold2=175)
cv.imshow(winname='canny_image', mat=canny_image)

# mode = cv.RETR_TREE if we want all heirachical contours
# mode = cv.RETR_EXTERNAL if we want only external contours
# mode = cv.RETR_LIST if we want all contours in image
# below method looks at the structuring element or the edges from the image and returns true values
# contours is a python list of all the coordinates of contours found in the image
# heirarchies it refers to heirarchical representation of contours
contours, hierarchies = cv.findContours(image=canny_image,mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours are found in the image using none method')

contours, hierarchies = cv.findContours(image=canny_image,mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are found in the image using simple method')

# just by blurring the image and using this as source for canny significantly reduces the number of contours

# threshold is another method to detect contours
# below method will look at an image and tries to binarize that image
# if intensity of a pixel is below 125 then it will be set to 0[black], if intensity is above 125 it will be set to 255[white]
ret, thresh = cv.threshold(src=gray_image,thresh=125, maxval=255, type=cv.THRESH_BINARY)
cv.imshow(winname='thresh_image', mat=thresh)

contours, hierarchies = cv.findContours(image=thresh,mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours are found in the image using threshold method')

# draw contours
cv.drawContours(image=blank_image, contours=contours, contourIdx=-1,color=(0,0,255), thickness=1)
cv.imshow(winname='draw_contour_image', mat=blank_image)

cv.waitKey(0)