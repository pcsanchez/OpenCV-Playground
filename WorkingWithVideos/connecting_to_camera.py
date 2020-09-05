import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# WINDOWS  -- *'DIVX'
# MACOS or LINUX *'XVID'

writer = cv2.VideoWriter('myvideo.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, heigth))

while True:

    ret, frame = cap.read()

    # OPERATIONS (DRAWING)
    writer.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()