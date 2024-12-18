import cv2

face_cascade = cv2.CascadeClassifier
rate = 10
img = cv2.imread('./img/children.jpg')


x,y,w,h = cv2.selectROI('mosaic', img, False)
if w and h:
    roi = img[y:y+h,x:x+w]
    roi = cv2.resize(roi,(w//rate, h//rate) )
    roi = cv2.resize(roi, (w, h))
    img[y:y+h, x:x+w] = roi
    cv2.imshow('mosaic', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



