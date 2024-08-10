import cv2
import imutils

img = cv2.imread("image/car1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray,(400,200))

bfiler = cv2.bilateralFilter(gray, 11 , 17 , 17)
edged = cv2.Canny(bfiler, 30 , 200)
rgb = cv2.cvtColor(gray_resize,cv2.COLOR_BGR2RGB)


keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours =  imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10 , True)
    if len(approx) == 4:
        location = approx
        break

print(location)

