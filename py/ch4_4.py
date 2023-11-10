import cv2

img = cv2.imread('apples.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

apples = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 150, param2 = 20,
                          minRadius = 50, maxRadius = 120) 
# 첫 번째 인수인 명암 영상에서 원을 검출해 중심과 반지름을 저장한 리스트를 반환
# 두 번째 인수는 여러 변형 알고리즘 중의 하나를 지정(cv.HOUGH_GRADIENT:에지 방향 정보를 추가로 사용하는 방법)
# 세 번째 인수는 누적 배열의 크기를 지정하는데 1로 설정하면 입력 영상과 같은 크기를 사용
# 네 번째 인수는 원 사이의 최소 거리를 지정하는데 작을수록 많은 원이 검출
# 다섯 번째 인수는 에지 알고리즘을 사용
# 여섯 번째 인수는 비최대 억제를 적용할 때 쓰는 임곗값
# 일곱, 여덟 번째 인수는 원의 최소와 최대 반지름을 지정

# 리스트가 가진 원의 중심과 반지름 정보를 이용해 원래 영상에 원을 그린다
for i in apples[0]:
    cv2.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 2)

cv2.imshow('Apple detection', img)

cv2.waitKey()
cv2.destroyAllWindows()