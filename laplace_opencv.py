import cv2.cv as cv

im = cv.LoadImage("/Users/liuchaochao/bird.jpeg", cv.CV_LOAD_IMAGE_COLOR)

gray = cv.CreateImage(cv.GetSize(im),8,1)
cv.CvtColor(im, gray, cv.CV_BGR2GRAY)

aperture=3

dst = cv.CreateImage(cv.GetSize(gray), cv.IPL_DEPTH_32F,1)
cv.Laplace(gray, dst, aperture)

cv.Convert(dst, gray)

thresholded = cv.CloneImage(im)
cv.Threshold(im, thresholded, 50, 255, cv.CV_THRESH_BINARY_INV)

cv.ShowImage('Laplace grayscale', gray)

cv.WaitKey(0)

