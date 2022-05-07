import cv2

#An image reading and showing
image = cv2.imread('nature.jpeg',0)
cv2.imshow('NatureImage',image)

#An image writing
cv2.imwrite('gri.png',image)


cv2.waitKey(0)
cv2.destroyWindow()