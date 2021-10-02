# Blur image
import cv2
import imutils

img = cv2.imread("resizeImg.png")
gaussianBlur = cv2.GaussianBlur(img, (21,21), 0)

cv2.imshow("gaussianBlur.png", gaussianBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()