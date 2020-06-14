# Resizing An Image
import cv2
import numpy as np

img = cv2.imread("resources/kirby.jpg")
print(img.shape)

imgResize = cv2.resize(img, (200, 200))
cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)

cv2.waitKey(0)