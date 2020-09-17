import cv2
import numpy as np

img = cv2.imread("res/Ford.jpg")
print(img.shape) # gives height and width

imgResize = cv2.resize(img,(350,200))
print(imgResize.shape)

#cv2.imshow("image",img)
cv2.imshow("image Resize",imgResize)

imgCropped = img[0:200,200:500]
cv2.imshow("cropped image",imgCropped)

cv2.waitKey(0)