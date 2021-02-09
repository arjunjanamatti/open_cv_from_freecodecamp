import os
import cv2 as cv
import numpy as np

people_list = []
for folder_name in os.listdir('train'):
    people_list.append(folder_name)

main_directory = 'train'

features = []
labels = []

def create_train(people_list):
    har_cas = cv.CascadeClassifier('har_face.xml')
    for person in people_list:
        path = os.path.join(main_directory,person)
        label = people_list.index(person)

        for img in os.listdir(path):
            color_image = os.path.join(path,img)
            img_matrix = cv.imread(color_image)
            gray_image = cv.cvtColor(src=img_matrix,code=cv.COLOR_BGR2GRAY)
            face_detect = har_cas.detectMultiScale(image=gray_image, scaleFactor=1.1, minNeighbors=3)
            for (x,y,w,h) in face_detect:
                faces_roi = gray_image[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train(people_list)
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and the labels list
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


