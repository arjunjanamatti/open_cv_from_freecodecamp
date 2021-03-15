import cv2 as cv

class ReadImages:
    def __init__(self):
        pass

    def display_image(self, image):
        self.image = image
        cv.imshow(winname='image_window', mat=self.image)
        cv.waitKey(0)

    def display_videos(self, video):
        self.video = video
        capture = cv.VideoCapture(self.video)
        while True:
            isTrue, frame = capture.read()
            cv.imshow(winname='play_video', mat=frame)
            if cv.waitKey(20) & 0xFF == ord('d'):
                break
        capture.release()
        cv.destroyAllWindows()

    def UseWebCam(self):
        capture = cv.VideoCapture(0)
        # define width
        capture.set(3, 640)
        # define height
        capture.set(4, 480)
        # define brightness
        capture.set(10,100)
        while True:
            isTrue, frame = capture.read()
            cv.imshow(winname='play_video', mat=frame)
            if cv.waitKey(20) & 0xFF == ord('d'):
                break
        capture.release()
        cv.destroyAllWindows()

image = cv.imread(filename = 'C:/Users/Arjun Janamatti/Documents/image_classification/nude_sexy_safe_v1_x320/testing/safe/0AFBAF6E-AC8F-4F86-B131-26AF632BF574.jpg')
video = 'C:/Users/Arjun Janamatti/PycharmProjects/jeeva_project/upload_videos/safe/video_2.mp4'
read_image = ReadImages()
# read_image.display_image(image)
# read_image.display_videos(video)
read_image.UseWebCam()


