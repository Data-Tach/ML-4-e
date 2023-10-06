
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np

img = cv2.imread("Pneumonia_02.jpeg",0)

img = cv2.resize(img, (500,600))

canny_edge = cv2.Canny(img,30,200)

sigma = 0.001

median = np.median(img)
lower = int(max(0,(1.0-sigma)*median))
upper = int(max(0,(1.0+sigma)*median))


auto_canny = cv2.Canny(img, lower, upper)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Image", canny_edge)
cv2.imshow(("Auto Canny Image"), auto_canny)



cv2.waitKey(0) 
cv2.destroyAllWindows() 
