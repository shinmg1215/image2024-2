import cv2
import numpy as np

img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)
thresh_np = np.zeros_like(img)
thresh_np[img > 127] = 255
thresh_np[ (128 < img)  & (img <= 171)] = 128
thresh_np[(64 < img)  &  (img <= 128)] = 64



thresh_np = np.zeros_like(img)
thresh_np[ img >64 ]=64
thresh_np[ img >128 ]=128
thresh_np[ img >171 ]=255

thresh_np = np.zeros_like(img)
ysize, xsize = img.shape
print(xsize)
print(img.shape)
for x in range(xsize):
    for y in range(ysize):
        if( img[y,x] > 64):
            thresh_np[y,x] = 64
        if (img[y,x] > 128):
            thresh_np[y,x] = 128
        if (img[y,x] > 171):
            thresh_np[y,x] = 255

print(img.shape)
x, v = img.shape
print(x)
#for x in range(img.shape.x)

_, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("thr", thresh_np)
cv2.imshow("img", img)
cv2.imshow("cv2", thresh_cv)
cv2.waitKey()
cv2.destroyAllWindows()