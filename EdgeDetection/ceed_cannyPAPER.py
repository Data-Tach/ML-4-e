import cv2
import mahotas
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
import mahotas
import math

img = mahotas.imread("covid-19_01.png")
img = img[:,:,0]

min = np.min(img)
max = np.max(img)


print("min",min)
print("max",max)

mxi = mahotas.locmax(img)
mni = mahotas.locmin(img)

mxils = []
for i,m in enumerate(mxi):
	ls = []
	for j,t in enumerate(m):
		if(t==True):
			ls.append(img[i][j])
		else:
			ls.append(min)
	mxils.append(ls)

mxils = np.array(mxils, dtype = 'uint8')


mnils = []
for i,m in enumerate(mni):
	ls = []
	for j,t in enumerate(m):
		if(t==True):
			ls.append(img[i][j])
		else:
			ls.append(max)
	mnils.append(ls)

mnils = np.array(mnils, dtype = 'uint8')

d1 = np.absolute(img-mxils)

d2 = np.absolute(img-mnils)



plt.imshow(img)
plt.savefig("originam_img.png")

plt.imshow(mxils)
# plt.show()
plt.savefig("maximg.png")



plt.imshow(mnils)
# plt.show()
plt.savefig("minimg.png")



plt.imshow(d1)
# plt.show()
plt.savefig("d1.png")

plt.imshow(d2)
# plt.show()
plt.savefig("d2.png")

if (d1<d2).all():
	img = mxils
else:
	img = mnils


plt.imshow(img)
# plt.show()
plt.savefig("P0.png")


# Gaussian function


std = np.std(img)

for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                G = (1.0/((2*np.pi*(std**2))**0.5))*math.exp(-((i**2 + j**2)/(2*(std**2))))
                img[i][j] = G * img[i][j]

plt.imshow(img)
plt.show()

print(img)



# print(mxils)

# print("--")

# print(mnils)

# cv2.imwrite("local_min_img.png", local_min_img)


# image = cv2.imread("Normal_01.jpeg",0)
# image = cv2.resize(image, (700,800))

# P0 = image

# Pmax = local_maximum_image(image)
# Pmin = local_minimum_image(image)

# D1 = np.absolute(P0 - Pmax)
# D2 = np.absolute(P0 - Pmin)



# cv2.imshow("Original Image", P0)

# cv2.imshow("Local Maximum Image", Pmax)

# cv2.imshow("Local Minimum Image", Pmin)

# cv2.imshow("Difference Maximum Image", D1)
# cv2.imshow("Difference Minimum Image", D2)


# if (D1<D2).all():
# 	print("central pixel is close to local_maximum_image")
# 	P0 = Pmax
# else:
# 	print("central pixel is close to local_minimum_image")	
# 	P0 = Pmin

# cv2.imshow("processed image", P0)





# cv2.waitKey(0)
# cv2.destroyAllWindows()
