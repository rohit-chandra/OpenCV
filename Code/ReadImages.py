import cv2

# img = cv2.imread("Resources/images/lena.jpg")

img = cv2.imread("D:/Code/Pycharm Projects/OpenCV/Open_CV/Resources/images/lena.jpg")

cv2.imshow("Lena", img)

# Add delay so that the image is displayed continuously

# waits for 1 second and then closes the image window
# cv2.waitKey(1000)


# wait for user to intervene otherwise keep on displaying the image
cv2.waitKey(0)
