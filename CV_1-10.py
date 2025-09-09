import cv2
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    vid_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', vid_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break