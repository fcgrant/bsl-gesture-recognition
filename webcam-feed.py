import cv2 as cv
from cv2 import VideoCapture


cv.namedWindow("preview")
video_feed: VideoCapture = cv.VideoCapture(0, cv.CAP_DSHOW)

video_feed.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
video_feed.set(cv.CAP_PROP_FRAME_HEIGHT, 720)


if video_feed.isOpened(): # try to get the first frame
    rval, frame = video_feed.read()
else:
    rval = False

while rval:
    cv.imshow("preview", frame)
    rval, frame = video_feed.read()
    key = cv.waitKey(20)
    if key == 27: # exit on ESC
        break

video_feed.release()
cv.destroyWindow("preview")