# thresh holdin image
import cv2
import imutils
img = cv2.imread("resizeImg.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresholdImg = cv2.threshold(grayImg, 120, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("lena", img)
cv2.imshow("grayImg", grayImg)
cv2.imshow("thresholdImg", thresholdImg)
cv2.imwrite("thresholdImg.png", thresholdImg)
cv2.waitKey(0)
cv2.destroyAllWindows()