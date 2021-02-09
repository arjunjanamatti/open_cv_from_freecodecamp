import numpy as np
import cv2 as cv
import os

# har_cas = cv.CascadeClassifier('har_face.xml')
#
# face_recognizer = cv.face.LBPHFaceRecognizer_create()
# face_recognizer.read('face_trained.yml')
#
# people_list = []
# for folder_name in os.listdir('train'):
#     people_list.append(folder_name)
#
# image_test = cv.imread('val\jerry_seinfeld\httpcdncdnjustjaredcomwpcontentuploadsheadlinesjerryseinfeldmakesbrianwilliamsjokejpg.jpg')
# gray_image = cv.cvtColor(src=image_test, code=cv.COLOR_BGR2GRAY)
# cv.imshow(winname='Person', mat=gray_image)
#
# # detect face in the image
# faces_rect = har_cas.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=3)
#
# for (x,y,w,h) in faces_rect:
#     faces_roi = gray_image[y:y+h,x:x+w]
#
#     label,confidence = face_recognizer.predict(faces_roi)
#     print(f'Label: {people_list[label]} with confidence: {confidence}')
#
#     cv.putText(image_test,text=str(people_list[label]),org=(20,20),fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1.0,color=(0,255,0),thickness=2)
#     cv.rectangle(image_test,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=2)
#
# cv.imshow(winname='Person', mat=image_test)
#
# cv.waitKey(0)

def get_result(image):
    har_cas = cv.CascadeClassifier('har_face.xml')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_trained.yml')

    people_list = []
    for folder_name in os.listdir('train'):
        people_list.append(folder_name)
    gray_image = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
    cv.imshow(winname='Person', mat=gray_image)
    # detect face in the image
    faces_rect = har_cas.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in faces_rect:
        faces_roi = gray_image[y:y + h, x:x + w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label: {people_list[label]} with confidence: {confidence}')

        cv.putText(image, text=str(people_list[label]), org=(20, 20), fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX,
                   fontScale=1.0, color=(0, 255, 0), thickness=2)
        cv.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

    cv.imshow(winname='Person', mat=image)

    cv.waitKey(0)

image_test = cv.imread('val\jerry_seinfeld\httpcdncdnjustjaredcomwpcontentuploadsheadlinesjerryseinfeldmakesbrianwilliamsjokejpg.jpg')
get_result(image_test)
