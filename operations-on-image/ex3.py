# grayscale image
import cv2
img = cv2.imread("lena.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("lena", img)
cv2.imshow("grayImg", grayImg)
cv2.imwrite("grayImg.png", grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()