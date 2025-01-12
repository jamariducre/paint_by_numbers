#Image-Processing-Fun
#This will be my first try at image processing code in python
#my hope is to start simple with just basic image processing
#such as filtering and then move up to eventually create a paint
#by numbers template for a portrait of my girlfriend.

#Jamari Ducre
#Wednesday, March 9th 2022

from cv2 import THRESH_BINARY
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2 as cv

imgBGR = cv.imread("cool_pic3.png")
img = cv.cvtColor(imgBGR, cv.COLOR_BGR2RGB)
grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

th1 = cv.adaptiveThreshold(grayImg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81,.01)

cv.namedWindow("Thresh1",cv.WINDOW_NORMAL)

cv.imshow("Thresh1",th1)

cv.waitKey(0)
cv.destroyAllWindows()