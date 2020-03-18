import  cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('1280.mp4')

while 1:
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face  = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,z) in face:
        cv2.rectangle(img,(x,y) ,(x+y,w+z), (255,0,0),2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

