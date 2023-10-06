import numpy as np
import cv2


img = cv2.imread("Pneumonia_01.jpeg", 0)
img = cv2.resize(img, (600,700))
edges = cv2.Canny(img,0.01,10)
#print(img)

#cv2.imshow("Original image", img)

cv2.imwrite("Pneumonia_01_edge.jpeg",edges)

cv2.imshow("Canny", edges)


cv2.waitKey(0)          
cv2.destroyAllWindows() 
