# Drawing shapes and adding text in an image
import cv2
import numpy as np

img = np.zeros((1024, 1024, 3), np.uint8)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,200,0), 3)
cv2.rectangle(img, (0,0), (250,550), (0,0,180), 3) # Area can be filled by cv2.FILLED
cv2.circle(img, (500,500), 100, (120,230,0), 5)
cv2.putText(img, "VAIBHAV", (300,250), cv2.FONT_HERSHEY_PLAIN , 5,(200,180,150))

cv2.imshow("Image", img)
cv2.waitKey(0)