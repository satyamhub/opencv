import cv2 as cv
import numpy as np
#create a blank image using numpy
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
#color the pixel of img(use only : for entire)
# blank[200:300, 300:400]=0,255,0
# cv.imshow('blank',blank)

#draw a rectangle
# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2) ,(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)
# #draw a circle
# cv.circle(blank, (blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=-1) #-1 to fill the circle
# cv.imshow('circle',blank)

# #draw line
# cv.line(blank, (0,50),(100,250),(255,0,0),thickness=10)
# cv.imshow('line',blank)

#write text
cv.putText(blank,'SATYAM',(255,255),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,70),2)
cv.imshow('text',blank)
cv.waitKey(0)
