import cv2
import matplotlib.pyplot as plt

img = cv2.imread('mistyroad.jpg') # 안개가 낀 도로 영상 읽기

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 명암 영상으로 변환
plt.imshow(gray, cmap ='gray'), plt.xticks([]), plt.yticks([]), plt.show() # 디스플레이

# 히스토그램을 구해 디스플레이
h = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(h, color = 'r', linewidth = 1), plt.show()

equal = cv2.equalizeHist(gray) # 명암 영상 gray에 히스토그램 평활화를 적용하고 결과 영상을 equal 객체에 저장
plt.imshow(equal, cmap = 'gray'), plt.xticks([]), plt.yticks([]), plt.show() # 디스플레이

h = cv2.calcHist([equal], [0], None, [256], [0, 256]) # equal영상의 히스토그램 구하기
plt.plot(h, color = 'r', linewidth = 1), plt.show() # 디스플레이