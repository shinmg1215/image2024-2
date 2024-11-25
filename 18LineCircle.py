from turtledemo.nim import COLOR

import cv2
import numpy as np

img = cv2.imread('./img/paper.jpg')

edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
print(lines)
if lines is not None:
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.cos(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 +1000 * (-b))
        y1 = int(x0 + 1000 * (a))
        x2 = int(x0 + 1000 * (-b))
        y2 = int(x0 + 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)



cv2.imshow('img', img)
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.imread('./img/sudoku.png')
edges = cv2.Canny(img, 50, 150, apertureSize=3)
linesp = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100)

print(linesp)
if linesp is not None:
    for line in linesp:
        x1, y1, x2, y2, = line[0]
        cv2.line(img, (x1,y1), (x2, y2), (0,0,255),2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('./img/coins_spread1.jpg',)
imgray = cv2.cvtColor(img, COLOR_BGR2GRAY)
circles = cv2.HoughCircles(imgray, method=cv2.HOUGH_GRADIENT,
                           dp=1, minDist=50, param2=120,
                           minRadius=10, maxRadius=100)
circles = np.int32(circles)
for circles in circles[0, :]:
    cx, cy, r = circles
    cv2.circle(img, (cx,cy),r,(0,0,255),2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
