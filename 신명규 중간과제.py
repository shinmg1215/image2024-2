import cv2

# 얼굴 검출을 위한 캐스케이드 분류기 생성
face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

# 검출할 이미지 읽고 그레이스케일로 변환
img = cv2.imread('./img/children.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print(f"Detected faces: {faces}")

# 얼굴 영역에 파란색 타원 그리기
for (x, y, w, h) in faces:
    center = (x + w//2, y + h//2)  # 타원의 중심
    axes = (w//2, h//2)            # 타원의 반경 (x축, y축)
    cv2.ellipse(img, center, axes, 0, 0, 360, (255, 0, 0), 2)  # 파란색 타원

    # 얼굴 영역 내에서 눈 검출
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
    print(f"Detected eyes: {eyes}")

    # 눈에 초록색 사각형 그리기
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # 초록색 네모

# 이미지 표시
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


