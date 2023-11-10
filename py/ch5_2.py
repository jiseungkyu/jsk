import cv2

# ������ �а� ��� �������� ��ȯ�Ͽ� ����
img = cv2.imread('mot_color70.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
# SIFT_create(nfeatures, nOctaveLayers, contrastThreshold, edgeThreshold, sigma)
# nfeatures: ������ Ư¡�� ������ ����(���⼭�� ����)
# nOctaveLayers: ��Ÿ�� ���� ����
# contrastThreshold: ���Ϸ� Ȯ������ �̼� ������ �� ���
# edgeThreshold: �������� ����� Ư¡���� �ɷ����� �� ���
# sigma: ��Ÿ�� 0�� �Է� ���� ������ ����þ��� ǥ������

# Ư¡���� ����ڸ� ã�� ��ü�� ����
kp, des = sift.detectAndCompute(gray, None)

gray = cv2.drawKeypoints(gray, kp, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # ������ Ư¡���� ���� ǥ��
cv2.imshow('sift', gray) #������ �����쿡 ��Ÿ��

k = cv2.waitKey()
cv2.destroyAllWindows()