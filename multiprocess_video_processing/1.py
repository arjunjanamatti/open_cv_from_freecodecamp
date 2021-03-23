import cv2 as cv
import time
import subprocess as sp
import multiprocessing as mp
from os import remove

file_name = 'arnold.mp4'
def process_video():
    # Read video file
    cap = cv.VideoCapture(file_name)

    # get height, width and frame count of the video
    width, height = (
        int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    )
    fps = int(cap.get(cv.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv.VideoWriter()
    output_file_name = "output_single.mp4"
    out.open(output_file_name, fourcc, fps, (width, height), True)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            im = frame
            # Perform face detection of frame
            _, bboxes = detectum.process_frame(im, THRESHOLD)

            # Loop through list (if empty this will be skipped) and overlay green bboxes
            for i in bboxes:
                cv.rectangle(im, (i[0], i[1]), (i[2], i[3]), (0, 255, 0), 3)

            # write the frame
            out.write(im)
    except:
        # Release resources
        cap.release()
        out.release()

    # Release resources
    cap.release()
    out.release()