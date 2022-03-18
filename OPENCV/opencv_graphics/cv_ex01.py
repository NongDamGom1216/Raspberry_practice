import numpy as np
import cv2
#모두 0으로 되어 있는 빈 Canvas(검정색)

img = np.zeros((512, 512, 3), np.uint8) # 0으로 초기화 (검은색 이미지)
# (y, x) unsigned int 8비트 : 1바이트
# img = np.zeros((512, 512, 3), np.uint8) + 255 # (흰색 이미지)

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5) # 색상 순서 -> (B, G, R)
cv2.rectangle(img, (384, 0), (510, 128), (0,255,0), 3) # 좌측 상단, 우측 하단, 색상, 선의 두께

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()