import cv2 as cv
import numpy as np

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0B16C26F-2C07-4F75-B8BC-F7A50E3D5EFE.jpg')
print('Shape of the image: ', img.shape)
cv.imshow(winname='image', mat=img)

# read the image
group_img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/training/sexy/GantMan_0A21E234-F4FF-49A7-B6AC-98C69F5C6EF2.jpg')
print('Shape of the image: ', group_img.shape)
cv.imshow(winname='group_img', mat=group_img)

# harcascade does not look at the skintone, they only look at object, it only looks at edges
gray_image = cv.cvtColor(src=group_img,code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='gray_image',mat=gray_image)

har_cas = cv.CascadeClassifier('har_face.xml')

# minNeighbors: number of neighbours rectangle should have to be called a face
faces_rect = har_cas.detectMultiScale(image=gray_image, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces in image is {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img=group_img,pt1=(x,y),pt2=(x+w,y+h), color=(0,255,0),thickness=2)
cv.imshow(winname='rectangle on face', mat=group_img)

cv.waitKey(0)
