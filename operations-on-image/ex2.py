# properties of image
import cv2
img = cv2.imread("lena.png")
print("Shape of image",img.shape)
print("Image of the size",img.size)
print("dtype of image",img.dtype)
cv2.destroyAllWindows()
