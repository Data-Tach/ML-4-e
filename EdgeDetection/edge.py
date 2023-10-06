import cv2
import numpy as np

image = cv2.imread("covid-19_01.png",0)

image = cv2.resize(image, (640,640))

cv2.imshow("Original Image", image)


cv2.waitKey(0)
cv2.destroyAllWindows()
