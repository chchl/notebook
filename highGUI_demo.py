import cv2.cv as cv

im = cv.LoadImage('/Users/liuchaochao/bird.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
threshold = cv.CreateImage(cv.GetSize(im), 8, 1)

def onChange(val):
    cv.Threshold(im, threshold, val, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage('Image', threshold)

onChange(100)
cv.CreateTrackbar('Thresh', 'Image',100,255,onChange)

cv.WaitKey(0)
