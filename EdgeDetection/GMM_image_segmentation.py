import numpy as np
import cv2

img = cv2.imread("covid-19_01.png")

img2 = img.reshape((-1,3))

from sklearn.mixture import GaussianMixture as GMM


n = 2
gmm_model = GMM(n, covariance_type='tied').fit(img2)

#print(gmm_model)

bic_values = gmm_model.bic(img2)
print(bic_values)

# gmm_labels = gmm_model.predict(img2)


# print(gmm_labels)

# original_shape = img.shape 

# segmentes = gmm_labels.reshape(original_shape[0], original_shape[1])

# cv2.imwrite("segmented_img.png", segmentes)


# cv2.waitKey(0)          
# cv2.destroyAllWindows() 


n_components = np.arange(1,10)

gmm_models = [GMM(n, covariance_type='tied').fit(img2) for n in n_components]

#print(gmm_models)


print(GMM.bic(img2))

from matplotlib import pyplot as plt
plt.plot(n_components, [m.bic(img2) for m in gmm_models], label='BIC')
plt.xlable('n_components')
