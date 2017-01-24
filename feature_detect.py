import cv2.cv as cv
import math

im = cv.LoadImage('/Users/liuchaochao/bird.jpeg', cv.CV_LOAD_IMAGE_GRAYSCALE)
im2 = cv.CloneImage(im)

eigImage = cv.CreateMat(im.height, im.width, cv.IPL_DEPTH_32F)
tempImage = cv.CloneMat(eigImage)

cornerCount = 500
quality = 0.01
minDistance = 10

corners = cv.GoodFeaturesToTrack(im, eigImage,tempImage, cornerCount, quality, minDistance)

radius = 3
thickness = 2

for (x,y) in corners:
    cv.Circle(im, (int(x), int(y)), radius, (255,255,255), thickness)

cv.ShowImage('GoodFeaturesToTrack',im)
cv.WaitKey(0)
