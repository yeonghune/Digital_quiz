import cv2
import numpy as np

img = cv2.imread('shapes.png')
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contour, hierarchy = cv2.findContours(imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


cv2.drawContours(img, contour, -1, (0,255,0), 4)
lst = ['Hexagon','Triangle','Pentagon','Circle','Rectangle']


for idex , i in enumerate(contour):
    cv2.putText(img,lst[idex],tuple(i[0][0],), cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)), 2)


cv2.imshow('CHAIN_APPROX_NONE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()