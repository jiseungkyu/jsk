import cv2

# 영상을 읽고 명암 영상으로 변환하여 저장
img = cv2.imread('mot_color70.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
# SIFT_create(nfeatures, nOctaveLayers, contrastThreshold, edgeThreshold, sigma)
# nfeatures: 검출할 특징점 개수를 지정(여기서는 생략)
# nOctaveLayers: 옥타브 개수 지정
# contrastThreshold: 테일러 확장으로 미세 조정할 때 사용
# edgeThreshold: 에지에서 검출된 특징점을 걸러내는 데 사용
# sigma: 옥타브 0의 입력 영상에 적용할 가우시안의 표준편차

# 특징점과 기술자를 찾아 객체에 저장
kp, des = sift.detectAndCompute(gray, None)

gray = cv2.drawKeypoints(gray, kp, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # 검출한 특징점을 영상에 표시
cv2.imshow('sift', gray) #영상을 윈도우에 나타냄

k = cv2.waitKey()
cv2.destroyAllWindows()