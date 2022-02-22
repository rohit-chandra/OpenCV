import cv2

img = cv2.imread("D:/Code/Pycharm Projects/OpenCV/Open_CV/Resources/images/frozen_lake.jpg")

# print the shape of image
# Original size of the image is (Height = 3024, Width = 4032, 3 channel BGR =3)
# height comes first and then the width in the array of images
print(img.shape)

width, height = 1000, 1000

# resize the image
imgResize = cv2.resize(img, (width, height))
print("After reshaping", imgResize.shape)

# cropping the image
# application: Self driving cars doesn't need the images above the road(like sky). So it's useful to crop the images

# [height, width]
imgCropped = img[1500:3000, 2500:4000]

# resize the crop image
# from the shape (3024, 4032, 3)
# Width = img.shape[1], Height = img.shape[0]
imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))
# display image
cv2.imshow("frozen_lake", img)
cv2.imshow("frozen_lake_reshape", imgResize)
cv2.imshow("Cropped frozen_lake", imgCropped)
cv2.imshow("Resize Cropped frozen_lake", imgCropResize)
# Add delay so that the image is displayed continuously
# wait for user to intervene otherwise keep on displaying the image
cv2.waitKey(0)
