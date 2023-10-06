# import cv2

# import numpy as np

# img = cv2.imread("orginal2.jpeg")

# img = cv2.resize(img, (500,600))

# cv2.imshow("Orginal Image", img)


# #Creating CLAHE 
# clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))

# #Apply CLAHE to the original image
# image_clahe_cv = clahe.apply(img)

# sigma = 0.5

# median = np.median(image_clahe_cv)
# lower = int(max(0,(1.0-sigma)*median))
# upper = int(max(0,(1.0+sigma)*median))

# canny = cv2.Canny(image_clahe_cv, lower, upper)


# cv2.imshow("Canny Image", canny)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


import numpy as np
import cv2


org = np.load("original.npy")

# print(org)

img = np.load("tmp.npy")

# cv2.imshow("winname", img)



sigma = 0.05

median = np.median(img)
lower = int(max(0,(1.0-sigma)*median))
upper = int(max(0,(1.0+sigma)*median))

canny = cv2.Canny(img, lower, upper)

# org = cv2.resize(org, canny.shape)

m1 = cv2.hconcat([org, img])

merged = cv2.hconcat([ m1 , canny])

# cv2.imshow("Canny Image", canny)

cv2.imshow("merged", merged)


cv2.imwrite("merged_original_enhanced.png", m1)

# cv2.imwrite("merged_enhanced_edge.png", merged)

cv2.imwrite("merged_enhanced_edge.png", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()

