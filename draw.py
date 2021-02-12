import cv2 as cv
import numpy as np

def readImage(img, window_name='original_image'):
    # display the read image
    cv.imshow(winname=window_name, mat=img)
    cv.waitKey(0)

# creation of blank image, here datatype 'uint8' image type
# height = 600, width = 400, number of color channels = 3
blank_image = np.zeros(shape=(600,400,3),dtype='uint8')

readImage(img=blank_image, window_name='Blank_image')

# 1. paint the image a certain color
blank_image[100:200, 100:200] = 0, 255,0
readImage(img=blank_image, window_name='Green background')

# 2. Draw a rectangle
cv.rectangle(img=blank_image, pt1=(0,0), pt2=(int(blank_image.shape[1]*0.5),int(blank_image.shape[0]*0.5)), color=(0,0,255), thickness=3)
readImage(img=blank_image, window_name='Green background')

# 2. Draw a rectangle
cv.rectangle(img=blank_image, pt1=(0,0), pt2=(int(blank_image.shape[1]*0.5),int(blank_image.shape[0]*0.5)), color=(0,0,255), thickness=cv.FILLED)
readImage(img=blank_image, window_name='Green background')

# 3. Draw a circle
cv.circle(img=blank_image, color=(0,0,255), thickness=cv.FILLED,center=(int(blank_image.shape[1]*0.5),int(blank_image.shape[0]*0.5)), radius = 50)
readImage(img=blank_image, window_name='Green background')

# 4. Draw a line
cv.line(img=blank_image, pt1=(0,0), pt2=(int(blank_image.shape[1]*0.5),int(blank_image.shape[0]*0.5)), color=(255,255,255), thickness=3)
readImage(img=blank_image, window_name='Green background')

# 5. write text on an image
cv.putText(img=blank_image, text='This just drawing things on a blank image',org=(0, int(blank_image.shape[0]*0.8)), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1.0, color=(0,0,255), thickness=2 )
readImage(img=blank_image, window_name='Green background')

class ImagesDraw:
    def __init__(self, image_path):
        self.image_path = image_path
        pass

    def ReadImage(self,window_name='original_image'):
        # display the read image
        image = cv.imread(self.image_path)
        cv.imshow(winname=window_name, mat=image)
        cv.waitKey(0)


    pass

