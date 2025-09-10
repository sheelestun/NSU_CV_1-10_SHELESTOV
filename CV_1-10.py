import cv2
import time
#Capturing your WEBcam
video_capture = cv2.VideoCapture(0)
#time counter
prevTime = 0
while True:
    _, frame = video_capture.read()
    vid_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#FPS
    nowTime = time.time()
    fps = 1 / (nowTime - prevTime)
    prevTime = nowTime
#image output on the screen
    cv2.putText(vid_gray, str(int(fps)), (0,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow('Video', vid_gray)
#shut down the prog
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#memory clear
video_capture.release()
cv2.destroyAllWindows()
