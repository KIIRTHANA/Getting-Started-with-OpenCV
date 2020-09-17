import cv2
import numpy as np

img = cv2.imread("res/img1.jpg")
kernel = np.ones((5,5),np.uint8) #matrix 5 by 5 all ones uint8(unsigned int of 8bit)

#convert into grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converts img to diff color bases
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #kernel size (odd numbers only),(7,7) size and value of matrix
#edge detector
imgCanny = cv2.Canny(img,200,200) #more the value, less the edges!
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #thickness of our edge will be increased to form clear lines
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) #erode opposite to dialation

#cv2.imshow("Grayimage",imgGray)
#cv2.imshow("Blurimg",imgBlur)
#cv2.imshow("Canny Image",imgCanny)
#cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)