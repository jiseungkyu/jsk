import skimage
import numpy as np
import cv2
import time

coffee = skimage.data.coffee()

start = time.time() # 시간 측정
slic = skimage.segmentation.slic(coffee, compactness=20, n_segments=600, start_label=1) # 영상을 분할해 객체에 저장
g = skimage.future.graph.rag_mean_color(coffee, slic, mode="similarity") # rag_mean_color: 슈퍼 화소를 노드로 사용, similarity:에지 가중치로 사용한 그래프를 구성하여 객체에 저장
ncut = skimage.future.graph.cut_normalized(slic, g)  # 정규화 절단
print(coffee.shape, " Coffee 영상을 분할하는데 ", time.time() - start, "초 소요")

marking = skimage.segmentation.mark_boundaries(coffee, ncut) # 영역 경계를 표시하고 객체에 저장
ncut_coffee = np.uint8(marking * 255.0) # unit8 형으로 변환

cv2.imshow("Normalized cut", cv2.cvtColor(ncut_coffee, cv2.COLOR_RGB2BGR))

cv2.waitKey()
cv2.destroyAllWindows()