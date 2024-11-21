import cv2 as cv

image = cv.imread('004.jpg')

resized_image = cv.resize(image, (200,200))

cv.imshow('Resized Image' , resized_image )

cv.waitKey(0)
cv.destroyAllWindows()