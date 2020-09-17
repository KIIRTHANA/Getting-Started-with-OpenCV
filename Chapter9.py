#detecting faces
import cv2

faceCascade = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")
img = cv2.imread("res/img1.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#bouding box to all faces

for(x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    

cv2.imshow("result",img)
cv2.waitKey(0)
