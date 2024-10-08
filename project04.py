import pylab
import cv2
import imutils
import numpy as np

img = cv2.imread("image/car1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray,(400,200))

bfiler = cv2.bilateralFilter(gray, 11 , 17 , 17)
edged = cv2.Canny(bfiler, 30 , 200)


keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours =  imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10 , True)
    if len(approx) == 4:
        location = approx
        break



mask = np.zeros(gray.shape,np.uint8)
new_image =  cv2.drawContours(mask,[location], 0 ,255 ,-1)
new_image = cv2.bitwise_and(img,img, mask=mask)
pylab.imshow(cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))
pylab.show()
