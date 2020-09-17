#Warp perspective
#have to work!!

import cv2
import numpy as np

img = cv2.imread("res/cards.jpeg")
#print(img.shape)

width,height = 212,250
pts1 = np.float32([[115,14],[236,34],[212,208],[86,187]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("images",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
