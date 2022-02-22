import cv2
import numpy as np

# size of kernel is 5*5 matrix having values 1,
# np.uint8(unsigned 8bits) is the type of data stored in this kernel
kernel = np.ones((5, 5), np.uint8)
print(kernel)
path = "D:/Code/Pycharm Projects/OpenCV/Open_CV/Resources/images/lena.jpg"

# read the image in grayscale by adding 0 in the parameter
# img = cv2.imread(path, 0)

img = cv2.imread(path)

# another method to convert image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# add blur to the image
# 5,5 is kernel value(it should only be in odd numbers. larger the number, more blurred the image
# kernel is a matrix that we iterate through the image to perform a function
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# shows the edges in the image
# 100 is the threshold parameters which control the amount of edges in th output image
# lesser the number, more will be the edges
imgCanny = cv2.Canny(imgBlur, 100, 100)

# image Dilation - increases the thickness of the edges from the uncanny image
# iteration value indicates the amount of thickness. more iteration value gives more thick edges of the images
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# image erosion - reverse of dilation
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# Show the image
cv2.imshow("Lena", img)
cv2.imshow("GrayScale", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilation", imgDilation)
cv2.imshow("Image Erosion", imgEroded)
cv2.waitKey(0)
