# Cropping An Image
import cv2
import numpy as np

img = cv2.imread("resources/dino.jpg")
print(img.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)