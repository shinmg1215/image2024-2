from retinaface import RetinaFace
import cv2

imgfile = './img/smilings.jpg'
resp = RetinaFace.detect_faces(imgfile)
print(resp)

image = cv2.imread(imgfile)

face1 = resp['face_1']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_2']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_3']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_4']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_5']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_6']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_7']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_8']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_9']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_10']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_11']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)

face1 = resp['face_12']
farea = face1['facial_area']
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255,0), 2)
cv2.putText(image, f"{face1['score']:.3f}", (farea[0], farea[1]),cv2.FONT_HERSHEY_PLAIN,
   2, (0,255,0),1)




cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()