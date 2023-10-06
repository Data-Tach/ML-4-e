import cv2
import mahotas
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time

def local_maximum_image(a):
	n,m = a.shape

	ls = []

	for i in tqdm(range(n),position=0, desc="i", leave=False, ncols=80):
		ls_ = []
		for j in tqdm(range(m),position=1, desc="j", leave=False, ncols=80):
			try:
				if a[i+1][j] <= a[i][j] and a[i-1][j] <= a[i][j] and a[i][j+1] <= a[i][j] and a[i+1][j-1] <= a[i][j]:
					ls_.append(a[i][j])
				else:
					ls_.append(0)
			except:
				ls_.append(0)
		ls.append(ls_.copy())

	return np.array(ls,dtype = 'uint8')

def local_minimum_image(a):
	n,m = a.shape

	ls = []

	for i in tqdm(range(n),position=0, desc="i", leave=False, ncols=80):
		ls_ = []
		for j in tqdm(range(m),position=1, desc="j", leave=False, ncols=80):
			try:
				if a[i+1][j] >= a[i][j] and a[i-1][j] >= a[i][j] and a[i][j+1] >= a[i][j] and a[i+1][j-1] >= a[i][j]:
					ls_.append(a[i][j])
				else:
					ls_.append(255)
			except:
				ls_.append(255)
		ls.append(ls_.copy())

	return np.array(ls,dtype = 'uint8')



image = cv2.imread("Normal_01.jpeg",0)
image = cv2.resize(image, (700,800))

P0 = image

Pmax = local_maximum_image(image)
Pmin = local_minimum_image(image)

D1 = np.absolute(P0 - Pmax)
D2 = np.absolute(P0 - Pmin)



# cv2.imshow("Original Image", P0)

# cv2.imshow("Local Maximum Image", Pmax)

# cv2.imshow("Local Minimum Image", Pmin)

# cv2.imshow("Difference Maximum Image", D1)
# cv2.imshow("Difference Minimum Image", D2)


if (D1<D2).all():
	print("central pixel is close to local_maximum_image")
	P0 = Pmax
else:
	print("central pixel is close to local_minimum_image")	
	P0 = Pmin

cv2.imshow("processed image", P0)





cv2.waitKey(0)
cv2.destroyAllWindows()