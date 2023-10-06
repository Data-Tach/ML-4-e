import cv2
import numpy as np


def util_function(filename):

	original_image = cv2.imread(filename)

	original_image = cv2.resize(original_image, (500,600))

	gaussian_blur_image = cv2.GaussianBlur(original_image, (5, 5), 0)

	sigma = 1

	median = np.median(gaussian_blur_image)
	lower = int(max(0,(1.0-sigma)*median))
	upper = int(max(0,(1.0+sigma)*median))

	auto_canny = cv2.Canny(gaussian_blur_image, 10, 100)


	cv2.imshow(f"Original Image {filename}", original_image)
	cv2.imshow(f"GaussianBlur Image {filename}", gaussian_blur_image)
	cv2.imshow(f"Canny Image {filename}", auto_canny)

	cv2.imwrite(f"canny_{filename}", auto_canny)

filenames = ["covid-19_01.png","Normal_01.jpeg"]

for filename in filenames:
	util_function(filename)

cv2.waitKey(0)
cv2.destroyAllWindows()
