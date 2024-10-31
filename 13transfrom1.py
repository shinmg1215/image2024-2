import cv2
import numpy as np


img = cv2.imread('./img/fish.jpg')
rows, cols = img.shape[0:2]

print(img.shpae)
print(f'={rows}')

dx, dy = 100, 50

mtrx = np.float32([1,0,dx], [0,1,dy])
dst = cv2.warpAffine(img, mtrx, cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT`

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()