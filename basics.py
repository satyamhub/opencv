import cv2 as cv

img=cv.imread('./photos/cat.jpg')
cv.imshow('cat',img)


#converting img to grayscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('blank',grey)

#blur an image
blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('bur',blur)

#edge cascade
canny=cv.Canny(img,125,275)
cv.imshow('edge cascade',canny)

# dialating the image
dialated=cv.dilate(canny,(9,9), iterations=3)
cv.imshow('dilated',dialated)

#eroding an image
eroded=cv.erode(dialated,(9,9),iterations=3)
cv.imshow('eroded',eroded)

#resizing an image
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resize)

#cropping an img
crop=img[50:200,200:400]
cv.imshow('resized',crop)
cv.waitKey(0)