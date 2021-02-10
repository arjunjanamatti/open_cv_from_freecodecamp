import cv2 as cv
import math

image_loc = 'angle_measure.jpg'
image = cv.imread(filename=image_loc)
points_list = []

def mouse_click_points(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img=image,center=(x,y),radius=5,color=(0,0,255),thickness=-1)
        points_list.append([x,y])
        print(points_list)
        # print(x,y)


cv.imshow(winname='angle_measure', mat=image)
cv.setMouseCallback('angle_measure', mouse_click_points)
cv.waitKey(0)

# https://www.youtube.com/watch?v=NmRt9kdUefk&list=PLMoSUbG1Q_r8vFXoAZPKyj-WLcD2aGoNZ
# https://github.com/murtazahassan?tab=repositories