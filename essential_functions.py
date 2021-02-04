import cv2 as cv

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)

cv.imshow(winname='image', mat=img)

# converting color to grayscale
gray_image = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image', mat=gray_image)

#  blur an image, can be used to blur some parts or noise
# to increase the blur, increase the kernel size
blur_image = cv.GaussianBlur(src=img, ksize=(7,7), sigmaX=cv.BORDER_DEFAULT)
cv.imshow(winname='blur_image', mat=blur_image)

# edge cascade: this is to find the edges in the image
# to reduce the number of images, we can use the blur image as source
canny_image = cv.Canny(image=blur_image, threshold1=125, threshold2=175)
cv.imshow(winname='canny_image', mat=canny_image)

# dilate the image using specific structural element: edges are structural element
dilated_image = cv.dilate(src=canny_image, kernel=(3,3), iterations=1)
cv.imshow(winname='dilated_image', mat=dilated_image)

# eroding the dilated image will get the edges back
eroded_image = cv.erode(src=dilated_image,kernel=(3,3),iterations=1)
cv.imshow(winname='eroded_image', mat=eroded_image)

# resize and crop an image
# INTER_AREA: interpolation is useful if we are shrinking the image to a smaller size than original one
# INTER_LINEAR or INTER_CUBIC: use it when we are enlarging the image
resize_image = cv.resize(src=img, dsize=(900,900), interpolation=cv.INTER_CUBIC)
cv.imshow(winname='resize_image', mat=resize_image)

cropping, like array slicing
cropped_image = img[50:200, 200:300]
cv.imshow(winname='cropped_image', mat=cropped_image)

cv.waitKey(0)