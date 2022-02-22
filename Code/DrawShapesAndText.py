import cv2

import numpy as np

# store 8bit unsigned values in the array
# outputs black image
img = np.zeros((512, 512, 3), np.uint8)

print("Shape of the image window", img.shape)

# BlueImg
# Blue = 255: Green = 0: Red = 0
# img[:] = 255, 0, 0

# draw a green diagonal line
# start point: point 1 = (0,0), End point: point2 = (width = img.shape[1], Height = img.shape[0])
# (Blue = 0, Green = 255, Red = 0)
# Thickness = 2
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

# Create a rectangle
# start point:(350, 100); End point: (450, 200)
# (Blue = 0, Green = 0, Red = 255)
# Thickness = 2
# cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), 2)

# fill the color of rectangle
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)

# draw circle
# center point = (150, 400); Radius = 50
cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)


# Print text on image
# Starting point: (75, 50)
# scale of font = 1
# Thickness = 1
cv2.putText(img, "Draw Shapes", (75, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow("Image", img)

cv2.waitKey(0)