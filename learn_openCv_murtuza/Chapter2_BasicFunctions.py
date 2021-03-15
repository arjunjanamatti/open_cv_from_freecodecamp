import cv2 as cv


image = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0AFBAF6E-AC8F-4F86-B131-26AF632BF574.jpg')

# convert grayscale
gray_image = cv.cvtColor(src=image,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='Gray image', mat=gray_image)
cv.waitKey(0)

