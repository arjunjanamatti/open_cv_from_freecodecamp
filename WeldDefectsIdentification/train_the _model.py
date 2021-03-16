import numpy as np
import cv2
import os
import random
import tensorflow as tf

h,w = 512,512
images = []
labels = []

files = os.listdir('./dataset/images/')
random.shuffle(files)

for f in files:
    img = cv2.imread('./dataset/images/' + f)
    parts = f.split('_')
    label_name = './dataset/labels/' + 'W0002_' + parts[1]
    label = cv2.imread(label_name,2)

    img = cv2.resize(img,(w,h))
    label = cv2.resize(label,(w,h))

    images.append(img)
    labels.append(label)

