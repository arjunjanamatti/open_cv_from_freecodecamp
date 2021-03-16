import numpy as np
import cv2
import os
import random
import tensorflow as tf

class UNetModel:
    def __init__(self, images_location, labels_location):
        self.images_location = images_location
        self.labels_location = labels_location
        pass

    def ImageResize(self):
        self.h, self.w = 512, 512
        self.images_list = []
        self.labels_list = []
        images_directory = os.listdir(self.images_location)
        random.shuffle(images_directory)
        for images in images_directory:
            img = cv2.imread(self.images_location + images)
            parts = images.split('_')
            label_name = self.labels_location + 'W0002_' + parts[1]
            label = cv2.imread(label_name, 2)

            img = cv2.resize(img, (self.w, self.h))
            label = cv2.resize(label, (self.w, self.h))

            self.images_list.append(img)
            self.labels_list.append(label)

        images = np.array(self.images_list)
        labels = np.array(self.labels_list)
        labels = np.reshape(labels,
                            (labels.shape[0], labels.shape[1], labels.shape[2], 1))

        print(images.shape)
        print(labels.shape)

        images = images / 255
        labels = labels / 255
        return images, labels

    def CreateModel(self):
        inputs = tf.keras.layers.Input(shape=(self.h, self.w, 3))

        conv1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same')(inputs)
        pool1 = tf.keras.layers.MaxPool2D()(conv1)

        conv2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(pool1)
        pool2 = tf.keras.layers.MaxPool2D()(conv2)

        conv3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(pool2)
        pool3 = tf.keras.layers.MaxPool2D()(conv3)

        conv4 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(pool3)

        upsm5 = tf.keras.layers.UpSampling2D()(conv4)
        upad5 = tf.keras.layers.Add()([conv3, upsm5])
        conv5 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(upad5)

        upsm6 = tf.keras.layers.UpSampling2D()(conv5)
        upad6 = tf.keras.layers.Add()([conv2, upsm6])
        conv6 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same')(upad6)

        upsm7 = tf.keras.layers.UpSampling2D()(conv6)
        upad7 = tf.keras.layers.Add()([conv1, upsm7])
        conv7 = tf.keras.layers.Conv2D(1, (3, 3), activation='relu', padding='same')(upad7)

        model = tf.keras.models.Model(inputs=inputs, outputs=conv7)

        return model

    def UseModel(self):
        images, labels = self.ImageResize()
        try:
            self.model = tf.keras.models.load_model('my_model')

        except:
            self.model = self.CreateModel()  # uncomment this to create a new model

            self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
            self.model.fit(images, labels, epochs=100, batch_size=10)
            self.model.evaluate(images, labels)

            self.model.save('my_model')
        pass

    def TestModel(self):
        num_cases = 3
        lowSevere = 1
        midSevere = 2
        highSevere = 4
        images_directory = os.listdir(self.images_location)
        random.shuffle(images_directory)
        for f in images_directory[0:num_cases]:
            test_img = cv2.imread(self.images_location + f)
            resized_img = cv2.resize(test_img, (self.w, self.h))
            resized_img = resized_img / 255
            cropped_img = np.reshape(resized_img,
                                     (1, resized_img.shape[0], resized_img.shape[1], resized_img.shape[2]))
            test_out = self.model.predict(cropped_img)

            test_out = test_out[0, :, :, 0] * 1000
            test_out = np.clip(test_out, 0, 255)

            resized_test_out = cv2.resize(test_out, (test_img.shape[1], test_img.shape[0]))
            resized_test_out = resized_test_out.astype(np.uint16)

            test_img = test_img.astype(np.uint16)

            grey = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

            for i in range(test_img.shape[0]):
                for j in range(test_img.shape[1]):
                    if (grey[i, j] > 150 & resized_test_out[i, j] > 40):
                        test_img[i, j, 1] = test_img[i, j, 1] + resized_test_out[i, j]
                        resized_test_out[i, j] = lowSevere
                    elif (grey[i, j] < 100 & resized_test_out[i, j] > 40):
                        test_img[i, j, 2] = test_img[i, j, 2] + resized_test_out[i, j]
                        resized_test_out[i, j] = highSevere
                    elif (resized_test_out[i, j] > 40):
                        test_img[i, j, 0] = test_img[i, j, 0] + resized_test_out[i, j]
                        resized_test_out[i, j] = midSevere
                    else:
                        resized_test_out[i, j] = 0

            M = cv2.moments(resized_test_out)
            maxMomentArea = resized_test_out.shape[1] * resized_test_out.shape[0] * highSevere
            print("0th Moment = ", (M["m00"] * 100 / maxMomentArea), "%")

            test_img = np.clip(test_img, 0, 255)

            test_img = test_img.astype(np.uint8)

            cv2.imshow(winname='Test Image',mat=test_img)

            cv2.waitKey(0)

        pass



image_location = './dataset/images/'
labels_location = './dataset/labels/'
image_net = UNetModel(image_location, labels_location)
image_net.UseModel()

# h,w = 512,512
# images_list = []
# labels_list = []
#
# images_directory = os.listdir('./dataset/images/')
# random.shuffle(images_directory)
#
# for images in images_directory:
#     img = cv2.imread('./dataset/images/' + images)
#     parts = images.split('_')
#     label_name = './dataset/labels/' + 'W0002_' + parts[1]
#     label = cv2.imread(label_name,2)
#
#     img = cv2.resize(img,(w,h))
#     label = cv2.resize(label,(w,h))
#
#     images_list.append(img)
#     labels_list.append(label)
#
# print(len(images_list), len(labels_list))
#
# images = np.array(images_list)
# labels = np.array(labels_list)
# labels = np.reshape(labels,
#     (labels.shape[0],labels.shape[1],labels.shape[2],1))
#
# print(images.shape)
# print(labels.shape)
#
# images = images/255
# labels = labels/255
#
# def create_model():
#
#     inputs = tf.keras.layers.Input(shape=(h,w,3))
#
#     conv1 = tf.keras.layers.Conv2D(16,(3,3),activation='relu',padding='same')(inputs)
#     pool1 = tf.keras.layers.MaxPool2D()(conv1)
#
#     conv2 = tf.keras.layers.Conv2D(32,(3,3),activation='relu',padding='same')(pool1)
#     pool2 = tf.keras.layers.MaxPool2D()(conv2)
#
#     conv3 = tf.keras.layers.Conv2D(64,(3,3),activation='relu',padding='same')(pool2)
#     pool3 = tf.keras.layers.MaxPool2D()(conv3)
#
#     conv4 = tf.keras.layers.Conv2D(64,(3,3),activation='relu',padding='same')(pool3)
#
#     upsm5 = tf.keras.layers.UpSampling2D()(conv4)
#     upad5 = tf.keras.layers.Add()([conv3,upsm5])
#     conv5 = tf.keras.layers.Conv2D(32,(3,3),activation='relu',padding='same')(upad5)
#
#     upsm6 = tf.keras.layers.UpSampling2D()(conv5)
#     upad6 = tf.keras.layers.Add()([conv2,upsm6])
#     conv6 = tf.keras.layers.Conv2D(16,(3,3),activation='relu',padding='same')(upad6)
#
#     upsm7 = tf.keras.layers.UpSampling2D()(conv6)
#     upad7 = tf.keras.layers.Add()([conv1,upsm7])
#     conv7 = tf.keras.layers.Conv2D(1,(3,3),activation='relu',padding='same')(upad7)
#
#     model = tf.keras.models.Model(inputs=inputs, outputs=conv7)
#
#     return model
#
# try:
#     model = tf.keras.models.load_model('my_model')
#
# except:
#     model = create_model()  # uncomment this to create a new model
#     print(model.summary())
#
#     model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
#     model.fit(images,labels,epochs=100,batch_size=10)
#     model.evaluate(images,labels)
#
#     model.save('my_model')