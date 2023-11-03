import cv2

img = cv2.imread('soccer.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 컬러 영상을 명암으로 변환

grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize = 3) # 결과 영상을 32비트 실수 맵에 저장, x 방향 연산자를 사용, 3*3 크기 사용
grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize = 3) # y 방향 연산자를 적용

# 음수가 포함된 맵에 절댓값을 취해 양수로 변환
sobel_x = cv2.convertScaleAbs(grad_x)
sobel_y = cv2.convertScaleAbs(grad_y)

edge_strength = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0) # sobel_x*0.5 + sobel_y*0.5 + 0

# 결과 영상을 윈도우에 디스플레이
cv2.imshow('Original', gray)
cv2.imshow('sobelx', sobel_x)
cv2.imshow('sobely', sobel_y)
cv2.imshow('edge strength', edge_strength)

cv2.waitKey()
cv2.destroyAllWindows()