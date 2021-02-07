import cv2 as cv
import numpy as np

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)
# color image consists of Red, Blue and Green channel, image is basically merge of these three channels

# blank image
blank_image = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(m=img)
cv.imshow(winname='Blue', mat=b)
cv.imshow(winname='Green', mat=g)
cv.imshow(winname='Red', mat=r)

print(f'Blue channel shape: {b.shape}\nGreen channel shape: {g.shape}\nRed channel shape: {r.shape}')

# merge images
merge_image = cv.merge(mv=[b,g,r])
cv.imshow(winname='merge_image', mat=merge_image)

# individual channels on blank image
blue_image = cv.merge(mv=[b,blank_image,blank_image])
green_image = cv.merge(mv=[blank_image,b,blank_image])
red_image = cv.merge(mv=[blank_image,blank_image,r])

cv.imshow(winname='blue_image', mat=blue_image)
cv.imshow(winname='green_image', mat=green_image)
cv.imshow(winname='red_image', mat=red_image)

cv.waitKey(0)