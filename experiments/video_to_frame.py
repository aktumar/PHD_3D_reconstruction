import cv2

vidcap = cv2.VideoCapture('video.mp4')


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image" + str(count) + ".jpg", image)  # save frame as JPG file
    return hasFrames


sec = 0
frameRate = 0.1  # it will capture image in each 1 second
count = 1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
