import cv2
from matplotlib import pyplot as plt
import pylab

img = cv2.imread("image/car1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray,(400,200))

bfiler = cv2.bilateralFilter(gray_resize, 11 , 17 , 17)
edged = cv2.Canny(bfiler, 30 , 200)
rgb = cv2.cvtColor(edged,cv2.COLOR_BGR2RGB)
pylab.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
pylab.show()