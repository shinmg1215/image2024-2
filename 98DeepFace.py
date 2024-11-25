import cv2
from charset_normalizer import detect
from deepface import DeepFace
from tensorboard.plugins.image.summary import image

img_file = "./img/children.jpg"
image = cv2.imread(img_file)

backends = ['opencv','ssd','dlib','mtcnn','fastmtcnn','retinaface','mediapipe','yolov8','yunet','centerface']
for engine in backends:
    print(engine)
    start = time.time()
    detections = DeepFace.extract_faces(img_path=img_file,
                                    detector_backend='mediaoip',
                                    enforce_detection=False)

#print(detections)
end = time.time()
timing.append((end-start)*1000)


for face in detections:
    facial_area = face['facial_area']
    print(facial_area)
    cv2.rectangle(image, (facial_area['x'], facial_area['y']),
                  (facial_area['x'] + facial_area['w'], facial_area['y'] + facial_area['h']),
                  (255, 0,0),2)


    cv2.imshow('img', manyimafes)
    cv2.imwrite('gradimage',  manyimafes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()