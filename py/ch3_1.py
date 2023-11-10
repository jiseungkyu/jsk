import cv2
import sys

img = cv2.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv2.imshow('original_RGV', img) # 세 채널을 가진 원래 영상 img를 'origin_RGB'라는 윈도우에 디스플레이
cv2.imshow('Upper left half', img[0:img.shape[0]//2,0:img.shape[1]//2,:]) # img의 왼쪽 위 부분을 잘라내어 'upper left half'윈도우에 디스플레이, ndarray 클래스의 슬라이싱 기능을 사용
cv2.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4,img.shape[1]//4:3*img.shape[1]//4,:]) # 첫번째와 두번째 축을 1/4부터 3/4까지 지정해 영상의 중간 부분을 잘라냄

# 영상을 채널별로 분리해 서로 다른 윈도우에 디스플레이
cv2.imshow('R channel', img[:,:,2])
cv2.imshow('G channel', img[:,:,1])
cv2.imshow('B channel', img[:,:,0])

cv2.waitKey()
cv2.destroyAllWindows()