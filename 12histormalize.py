import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None,[256], [0,255])
plt.plot(hist)
plt.show()

#img_norm = ((img - img.min() * 255.0)  /  (img.max() - img.min()))

#img_norm = ((img - img.min() * 255.0)  /  (img.max() - img.min()))

#img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

img_f = img.astype(np.float32)
img_norm = (img_f - img_f.min)

hist_norm = cv2.calcHist([img_norm], [0], None, [256],)


plt.subplot(1,2,0)
plt.plot(hist_norm)
plt.subplot(1,2,1)
plt.plot(hist_normcv)
plt.show()
print(img_norm)
cv2.imshow('', img)
cv2.imshow('imgnorm', img_norm.astype(np.uint8))
cv2.imshow('imgnorm_cv', img_normcv)
cv2.waitKey(0)
cv2.destroyAllWindows()
