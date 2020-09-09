# Face detection using Haar Cascades and Viola-Jones
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img):
    plt.imshow(img, cmap='gray')
    plt.show()

nadia = cv2.imread('../DATA/Nadia_Murad.jpg', 0)
denis = cv2.imread('../DATA/Denis_Mukwege.jpg', 0)
solvay = cv2.imread('../DATA/solvay_conference.jpg', 0)

face_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10)
    return face_img

def adj_detect_face(img):
    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10)
    return face_img

result = adj_detect_face(solvay)
display(result)

eye_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_eye.xml')

def detect_eyes(img):
    eye_img = img.copy()

    eye_rects = eye_cascade.detectMultiScale(eye_img)
    for (x,y,w,h) in eye_rects:
        cv2.rectangle(eye_img, (x,y), (x+w,y+h), (255,255,255), 10)
    return eye_img

result = detect_eyes(denis)
display(result)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = detect_face(frame)

    cv2.imshow('Video Face Detect', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()