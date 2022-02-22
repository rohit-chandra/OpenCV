import cv2

# For video

frameWidth = 640
frameHeight = 360

# read the video form the location
capVideo = cv2.VideoCapture("D:/Code/Pycharm Projects/OpenCV/Open_CV/Resources/videos/skiing_video.mp4")

# declare loop to read each frame

while True:
    # success is a flag which tells us whether the frame is captured successfully or not
    # img will store the frames of the video
    success, imgFrame = capVideo.read()
    # resize the window to any width and height
    imgFrame = cv2.resize(imgFrame, (frameWidth, frameHeight))
    cv2.imshow("Skiing", imgFrame)

    # if you press q then the loop breaks, Video stops playing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

