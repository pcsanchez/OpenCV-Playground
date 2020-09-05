import cv2

# Callback function rectangle
def draw_rectangle(event, x, y, flags, param):

    global pt1, pt2, topLeftClicked, bottomRightClicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # Reset the rectangle
        if topLeftClicked and bottomRightClicked:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeftClicked = False
            bottomRightClicked = False

        if topLeftClicked == False:
            pt1 = (x,y)
            topLeftClicked = True

        elif bottomRightClicked == False:
            pt2 = (x,y)
            bottomRightClicked = True

# Global variables
pt1 = (0,0)
pt2 = (0,0)
topLeftClicked = False
bottomRightClicked = False

# Connect to the callback
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top left corner.
x = width // 2
y = height // 2

# Width and height of rectangle
w = width // 4
h = height // 4

# Bottom right corner x + w, y + h

while True:

    ret, frame = cap.read()

    # Drawing on the frame based on global variables
    if topLeftClicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)

    if topLeftClicked and bottomRightClicked:
        cv2.rectangle(frame, pt1, pt2, color=(0,0,255), thickness=3)

    cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255), thickness=4)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()