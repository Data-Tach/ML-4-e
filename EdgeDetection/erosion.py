# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np

# Reading the input image
img = cv2.imread('covid-19_01.png', 0)

img1 = cv2.imread('Normal_01.jpeg', 0)

img = cv2.resize(img, (500,600))
img1 = cv2.resize(img1, (500,600))

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_erosion1 = cv2.erode(img1, kernel, iterations=1)

img_dilation = cv2.dilate(img, kernel, iterations=1)
img_dilation1 = cv2.dilate(img1, kernel, iterations=1)

cv2.imshow('Input Original Covid', img)
cv2.imshow('Erosion Original Covid', img_erosion)
cv2.imshow('Dilation Original Covid', img_dilation)

cv2.imshow('Input Original Normal', img1)
cv2.imshow('Erosion Original Normal', img_erosion1)
cv2.imshow('Dilation Original Normal', img_dilation1)


cv2.waitKey(0)
cv2.destroyAllWindows()