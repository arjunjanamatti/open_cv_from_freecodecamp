import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# # read image using RGB
# plt.imshow(img)
# plt.show()

# convert bgr to grayscale
gray_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image', mat=gray_image)

# convert BGR to HSV
hsv_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2HSV)
cv.imshow(winname='hsv_image', mat=hsv_image)

# BGR to L*a*b
lab_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2LAB)
cv.imshow(winname='lab_image', mat=lab_image)

# BGR to RGB
rgb_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2RGB)
cv.imshow(winname='rgb_image', mat=rgb_image)

# HSV to bgr
bgr_image = cv.cvtColor(src=hsv_image,code=cv.COLOR_HSV2BGR)
cv.imshow(winname='bgr_image', mat=bgr_image)

# L*a*b to bgr
bgr_from_lab_image = cv.cvtColor(src=lab_image,code=cv.COLOR_Lab2BGR)
cv.imshow(winname='bgr_from_lab_image', mat=bgr_from_lab_image)

cv.waitKey(0)