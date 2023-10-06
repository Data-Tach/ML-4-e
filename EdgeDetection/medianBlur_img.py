import cv2
import numpy as np


def util_function(filename):

	original_image = cv2.imread(filename)

	original_image = cv2.resize(original_image, (500,600))

	median_blur = cv2.medianBlur(original_image, 5)
	sigma = 1

	median = np.median(median_blur)
	lower = int(max(0,(1.0-sigma)*median))
	upper = int(max(0,(1.0+sigma)*median))

	auto_canny = cv2.Canny(median_blur, 10, 100)


	cv2.imshow(f"Original Image {filename}", original_image)
	cv2.imshow(f"MedianBlur Image {filename}", median_blur)
	cv2.imshow(f"Canny Image {filename}", auto_canny)

	cv2.imwrite(f"medianBlur_canny_{filename}", auto_canny)

# filenames = ["covid-19_01.png","covid-19_02.jpg","covid-19_03.png","Normal_01.jpeg","Normal_02.jpeg"]

# for filename in filenames:
	# util_function(filename)
util_function("D:\\JYOTHIPRAKASH\\desktop\\MLPaperPre\\EdgeDetection\\original\\orginal2.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
