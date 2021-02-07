import cv2 as cv
import numpy as np

blank_image = np.zeros((500,500), dtype='uint8')

rectangle_draw = cv.rectangle(img=blank_image.copy(),pt1=(0,0),pt2=(300,300), color=255, thickness=-1)
circle_draw = cv.circle(img=blank_image.copy(), center=(250,250), radius=100, color=255, thickness=-1)
# Four basic bitwise operators:
# AND
# OR
# XOR
# NOT

cv.imshow(winname='rectangle_draw', mat=rectangle_draw)
cv.imshow(winname='circle_draw', mat=circle_draw)

# bitwise AND: it returns only intersecting regions
bitwise_and = cv.bitwise_and(src1=rectangle_draw,src2=circle_draw)
cv.imshow(winname='bitwise_and', mat=bitwise_and)

# bitwise OR: it returns the intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(src1=rectangle_draw,src2=circle_draw)
cv.imshow(winname='bitwise_or', mat=bitwise_or)

# bitwise XOR: it returns only non-intersecting regions
bitwise_xor = cv.bitwise_xor(src1=rectangle_draw,src2=circle_draw)
cv.imshow(winname='bitwise_xor', mat=bitwise_xor)

# bitwise NOT: inverts the colors
bitwise_not = cv.bitwise_not(src=rectangle_draw)
cv.imshow(winname='bitwise_not', mat=bitwise_not)

cv.waitKey(0)