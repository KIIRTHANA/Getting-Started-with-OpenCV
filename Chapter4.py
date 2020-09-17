import cv2
import numpy as np

#using numpy create matrix

img = np.zeros((412,412,3),np.uint8) # 3 is for bgr
#print(img)
#img[200:300,100:300]=0,255,0
#img[:]=255,0,145 #purple

#cv2.line(img,(0,10),(250,150),(0,255,200),3) #normal line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,200),3)
cv2.rectangle(img,(0,0),(200,250),(255,0,150),cv2.FILLED)
cv2.circle(img,(250,50),30,(255,230,0),5)
cv2.putText(img,"HELLO, It's openCV!",(80,120),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,200,255),2)


cv2.imshow("Image",img)



cv2.waitKey(0)