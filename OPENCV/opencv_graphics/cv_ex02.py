# Circle

import cv2
import numpy as np

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8) + 255 # 흰색 배경
# shape가 튜플 형태로 -> y축, x축 
cy = img.shape[0] // 2 # 몫
cx = img.shape[1] // 2

# 인수 3개 - 세 번째 인수는 숫자 사이의 거리를 말한다. -> [200, 100]
for r in range(200, 0, -100):
    cv2.circle(img, (cx, cy), r, color = (255, 0, 0))

cv2.circle(img, (cx, cy), radius=50, color=(0, 0, 255), thickness = -1)
# 굵기 = -1 : 면을 채워라

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()