import cv2 as cv
import math

image_loc = 'angle_measure.jpg'
points_list = []
image = cv.imread(filename=image_loc)


def mouse_click_points(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img=image,center=(x,y),radius=5,color=(0,0,255),thickness=-1)
        points_list.append([x,y])
        print(points_list)
        # print(x,y)

def get_slope(pt1,pt2):
    # slope = (y_2 - y_1) / (x_2 - x_1)
    slope = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
    return slope

def get_angle(points_list):
    pt1,pt2,pt3 = points_list[-3:]
    m_1 = get_slope(pt1,pt2)
    m_2 = get_slope(pt1, pt3)
    x = (m_1 - m_2)/(1 + (m_1 * m_2))
    angle_radian = math.atan(math.fabs(x))
    angle_degrees = round(math.degrees(angle_radian))
    print(angle_degrees)
    return angle_degrees

while True:

    if (len(points_list) % 3 == 0) & (len(points_list) != 0):
        get_angle(points_list)
        cv.putText(image, text=str(get_angle(points_list)), org=(points_list[-3][0], points_list[-3][1]), fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX,
                   fontScale=1.0, color=(0, 255, 0), thickness=2)
        # cv.putText(img=image, text=str(get_angle(points_list)), org=points_list[-3], fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX,
        #            fontScale=1.0, color=(0, 255, 0), thickness=2)

    cv.imshow(winname='angle_measure', mat=image)
    cv.setMouseCallback('angle_measure', mouse_click_points)
    # if we press q, the points will be reset
    if cv.waitKey(1) & 0xFF==ord('q'):
        points_list = []
        image = cv.imread(filename=image_loc)

# https://www.youtube.com/watch?v=NmRt9kdUefk&list=PLMoSUbG1Q_r8vFXoAZPKyj-WLcD2aGoNZ
# https://github.com/murtazahassan?tab=repositories