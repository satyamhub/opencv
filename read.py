import cv2 as cv
#image read
# img=cv.imread('./photos/cat.jpg')

# cv.imshow('Cat',img)

# cv.waitKey(0)

#video read
capture=cv.VideoCapture('./videos/video.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
