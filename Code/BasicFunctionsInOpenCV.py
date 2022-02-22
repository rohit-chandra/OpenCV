import cv2

path = "images/lena.jpg"

# read the image in grayscale by adding 0 in the parameter
img = cv2.imread(path, 0)

# another method to convert image to grayscale
cv2.imshow("Lena", img)
cv2.waitKey(0)