import cv2
import imutils

img = cv2.imread("lena.png")
resizeImg = imutils.resize(img,width=300)
cv2.imwrite("resizeImg.png", resizeImg)