import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

blank_image = np.zeros(shape=img.shape[:2], dtype='uint8')

# Histogram allows us to visualize the distribution of pixel intensity in an image

gray_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image', mat=gray_image)

# draw circle over the mask
mask_image = cv.circle(img=blank_image, center=(img.shape[1]//2+70, img.shape[0]//2),radius=100, color=255,thickness=-1)
# cv.imshow(winname='mask_image', mat=mask_image)

# masking the image
masked_image = cv.bitwise_and(src1=gray_image, src2=gray_image, mask=mask_image)
cv.imshow(winname='masked_image', mat=masked_image)

# grayscale histogram
gray_hist = cv.calcHist(images=[gray_image], channels=[0], mask=masked_image,histSize=[256], ranges=[0,256])

plt.figure()
plt.title('Gray scale image histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# color histogram
colors = ('b','g','r')
plt.figure()
plt.title('Color BGR image histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')

for index, color in enumerate(colors):
    color_hist = cv.calcHist(images=[img], channels=[index], mask=None,histSize=[256], ranges=[0,256])
    plt.plot(color_hist)
    plt.xlim([0, 256])
plt.show()

    

cv.waitKey(0)