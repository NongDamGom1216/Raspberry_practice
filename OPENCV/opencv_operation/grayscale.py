import cv2
# import numpy as np

img = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[120, 200] = 0 # 화소값(밝기, 그레이스케일) 변경 (y축, x축)
# print(img[100:110, 200:210]) # ROI 접근(관심 영역 접근)
#(y축, x축)에 대한 슬라이싱

# img2 = img[100:300, 100:200]
# 복사본을 만드는 것이 아님, 원본 하나로 작업한다.

img2 = img[100:300, 100:200].copy() # 복사본

# img[100:400, 200:300] = 0 # ROI 접근
# 이거랑 같은 뜻인듯?
# for y in range(100, 400):
#     x in range(200, 300):
#         img[y, x] = 0

cv2.imshow('img', img)
cv2.imshow('img2', img2) # 그림의 일부 영역
cv2.waitKey()
cv2.destroyAllWindows()