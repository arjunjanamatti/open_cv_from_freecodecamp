import cv2 as cv




def rescaleFrame(frame, scale = 0.75):
    '''
    frame: matrix from reading the image
    scale: float for transformation from original image
    '''
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(src=frame, dsize=dimensions, interpolation=cv.INTER_AREA)

def readImage(img, window_name='original_image'):
    # display the read image
    cv.imshow(winname=window_name, mat=img)
    cv.waitKey(0)

# read the image
img = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0AFBAF6E-AC8F-4F86-B131-26AF632BF574.jpg')
print('Shape of the image: ', img.shape)

image_resize = rescaleFrame(frame=img)
print('Shape of the image: ', image_resize.shape)

readImage(img)
readImage(image_resize, window_name='resized_image')

# reading videos
capture = cv.VideoCapture('C:/Users/Arjun Janamatti/PycharmProjects/jeeva_project/upload_videos/video_2.mp4')

while True:
    isTrue, orig_frame = capture.read()
    resize_frame = rescaleFrame(frame=orig_frame, scale=0.5)
    cv.imshow('Video play', orig_frame)
    cv.imshow('Resize video play', resize_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()




