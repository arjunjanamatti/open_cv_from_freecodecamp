import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)
# color image consists of Red, Blue and Green channel, image is basically merge of these three channels

b,g,r = cv.split(m=img)
cv.imshow(winname='Blue', mat=b)
cv.imshow(winname='Green', mat=g)
cv.imshow(winname='Red', mat=r)

print(f'Blue channel shape: {b.shape}\nGreen channel shape: {g.shape}\nRed channel shape: {r.shape}')



cv.waitKey(0)