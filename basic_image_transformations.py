import cv2 as cv
import numpy as np

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0A556B72-059A-4BFE-AA28-80728C324749.jpg')
print('Shape of the image: ', img.shape)

cv.imshow(winname='image', mat=img)

# translation: basically shifting the image along x and y axis
def translate_image(img,x,y):
    trans_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(src=img, M=trans_matrix, dsize=dimensions)

# -x --> left
# +x --> right
# -y --> up
# +y --> down
translate = translate_image(img, -100, 100)
cv.imshow(winname='translateimage', mat=translate)

# rotation: will rotate at a certain angle
def rotate_image(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint==None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(center=rotPoint, angle = angle, scale = 1.0)
    dimensions=(width,height)

    return cv.warpAffine(src=img, M=rotMat, dsize=dimensions)

# positive angle will rotate anticlockwise
# negative angle will rotate clockwise

rotated = rotate_image(img,-45)
cv.imshow(winname='rotatedimage', mat=rotated)

rotated_to_rotated = rotate_image(rotated,45)
cv.imshow(winname='rotated_to_rotated', mat=rotated_to_rotated)

# resizing
resized = cv.resize(src=img,dsize=(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow(winname='resized', mat=resized)

# flipping an image
# flipcode = 0, implies flipping the image vertically along x axis
# flipcode = -1, implies flipping the image horizontally along y axis
# flipcode = 1, implies flipping the image horizontally and vertically
flip_image = cv.flip(src=img, flipCode=-1)
cv.imshow(winname='flip_image', mat=flip_image)

# cropping, like array slicing
cropped_image = img[50:200, 200:300]
cv.imshow(winname='cropped_image', mat=cropped_image)

cv.waitKey(0)