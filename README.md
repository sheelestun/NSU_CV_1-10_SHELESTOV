Программа выводит на экран изображение с Вебкамеры в чернобелом цвете с счеткчиком кадров в секунду
Для работы необходим Python версии 3.9 и новее
video_capture = cv2.VideoCapture(<"sign">) - захватывает изображение с вашей вебкамеры, где параметре sign - номер устройства(по умолчанию 0, но может отличаться)

#FPS - подсчет кадров в секунду
    nowTime = time.time()
    fps = 1 / (nowTime - prevTime)
    prevTime = nowTime

#image output to the screen - вывод изображения с количеством FPS на экран
 
   cv2.putText(vid_gray, str(int(fps)), (0,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('Video', vid_gray)

#memory clear - очистка памяти после работы с камерой

    video_capture.release()
    cv2.destroyAllWindows()
