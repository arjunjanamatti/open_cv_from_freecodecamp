import cv2 as cv
import numpy as np

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# Masking: Allows us to focus on certain parts of image, where we want to focus
blank_image = np.zeros(shape=img.shape[:2], dtype='uint8')
cv.imshow(winname='blank_image', mat=blank_image)

# draw circle over the mask
mask_image = cv.circle(img=blank_image, center=(img.shape[1]//2, img.shape[1]//2),radius=100, color=255,thickness=-1)
cv.imshow(winname='mask_image', mat=mask_image)

masked_image = cv.bitwise_and(src1=img, src2=img, mask=mask_image)
cv.imshow(winname='masked_image', mat=masked_image)

# size of mask can be max the size of image

cv.waitKey(0)