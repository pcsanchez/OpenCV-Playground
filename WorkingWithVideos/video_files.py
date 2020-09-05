import cv2
import time

cap = cv2.VideoCapture('myvideo.avi')

if cap.isOpened() == False:
    print('Error: File not found or wrong codec used!')

while cap.isOpened():

    ret, frame = cap.read()

    if ret == True:

        # Writer 20 fps
        time.sleep(1/20)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()