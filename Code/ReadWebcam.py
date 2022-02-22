import cv2

# For video

frameWidth = 640
frameHeight = 480

# read through default camera
capVideoCam = cv2.VideoCapture(0)
# 3 is default width & 4 is default height defined by openCV
capVideoCam.set(3, frameWidth)
capVideoCam.set(4, frameHeight)

# declare loop to read each frame

while True:
    # success is a flag which tells us whether the frame is captured successfully or not
    # img will store the frames of the video
    success, img = capVideoCam.read()

    cv2.imshow("Skiing", img)

    # if you press q then the loop breaks, Video stops playing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

