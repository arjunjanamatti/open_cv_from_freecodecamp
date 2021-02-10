import os
import caer
import numpy as np
import cv2 as cv2
from glob import glob
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import LearningRateScheduler
import canaro
import sklearn.model_selection as skm
import matplotlib.pyplot as plt


image_size = (80,80)
# gray scale image, hence only 1 channel
channels = 1
base_path = 'simposons/simpsons_dataset'

trial_dict = {}

for file in os.listdir(base_path):
    subfile_path = os.path.join(base_path,file)
    subfiles = glob('{}/*'.format(subfile_path))
    # print(file, len(subfiles))
    trial_dict[file] = len(subfiles)

print(trial_dict)
# sort in descending order
trial_dict = caer.sort_dict(unsorted_dict=trial_dict,descending=True)
print(trial_dict)

characters = []
count = 0
for keys in trial_dict:
    characters.append(keys[0])
    count +=1
    if count > 10:
        break
    
print(characters)

# create a training data
train = caer.preprocess_from_dir(DIR=base_path,classes=characters,IMG_SIZE=image_size,channels=channels,isShuffle=True)

print(f'Number of images used for training: {len(train)}')

# seperate features and labels
features, labels = caer.sep_train(data=train,IMG_SIZE=image_size,channels=channels)

# normalize the features and we have to labels from numerical integers to one hot encode
features = caer.normalize(features)
labels = to_categorical(y=labels,num_classes=len(characters))
split_data = skm.train_test_split(features, labels, test_size=.2)
x_train, x_val, y_train, y_val = (np.array(item) for item in split_data)

del train
del features
del labels

# image data generator
Batch_SIZE = 32
datagen = canaro.generators.imageDataGenerator()
train_gen = datagen.flow(x_train,y_train,batch_size=Batch_SIZE)

# creation of model
model = canaro.models.createSimpsonsModel(IMG_SIZE=image_size,
                                          channels=channels,
                                          output_dim=len(characters),
                                          loss='binary_crossentropy',
                                          decay=1e-6,
                                          learning_rate=0.001,
                                          momentum=0.9,
                                          nesterov=True)

print(model.summary())

# callbacks
callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]

# train the model
training = model.fit(x=train_gen,steps_per_epoch=len(x_train)/Batch_SIZE,epochs=10,validation_data=(x_val,y_val),validation_steps=len(y_train)/Batch_SIZE, callbacks=callbacks_list)

img = cv.imread(test_path)

plt.imshow(img)
plt.show()

def prepare(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.resize(image, IMG_SIZE)
    image = caer.reshape(image, IMG_SIZE, 1)
    return image

predictions = model.predict(prepare(img))

# Getting class with the highest probability
print(characters[np.argmax(predictions[0])])