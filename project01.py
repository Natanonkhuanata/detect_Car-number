import cv2
from matplotlib import pyplot as plt
#import easyocr

img = cv2.imread("image/car1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(gray,cv2.COLOR_BGR2RGB)
cv2.imshow("Output",rgb)
cv2.waitKey(0)
