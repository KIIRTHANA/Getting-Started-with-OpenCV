import cv2
import numpy as np

'''
print("package imported")
img = cv2.imread("res/image1.png")
cv2.imshow("Output",img)
cv2.waitKey(4000) #1000=1sec
'''
cap = cv2.VideoCapture(0) #default webcam (0)
cap.set(3,640)
cap.set(4,480) #size of window
cap.set(10,100) # id for brightness is 10
#videos are just series of images, we'll use a while loop for it to go frame by frame

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




