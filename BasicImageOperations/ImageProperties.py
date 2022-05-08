import cv2
import numpy as np

#Reading image
img = cv2.imread('football.jpg')

print(str(img.item(100,100,0)))
img.itemset((100,100,2),255)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
