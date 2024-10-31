import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows, cols = img.shape[0:2]

#d10 = 10 / 360*4.14
#d10 = (10*3.14)/180

d10 = (10 * np.pi) /180
d45 = (45 * np.pi) /180
d90 = (90 * np.pi) /180


m10 = np.float32([[np.cos(d10),-1 * np.sin(d10),0],
        [np.sin(d10), np.cos(d10),0]])

m45 = np.float32([[np.cos(d45),-1 * np.sin(d45),0],
        [np.sin(d45), np.cos(d45),0]])

m90 = np.float32([[np.cos(d90),-1 * np.sin(d90),0],
        [np.sin(d90), np.cos(d90),0]])


m90 = np.float32([[0,1,0],
                  [1, 0, 0]])
r90 = cv2.warpAffine(img, m10, (rows,cols))

cv2.imshow('img', img)
cv2.imshow('r90',r90)
cv2.waitKey(0)
cv2.destroyAllWindows()