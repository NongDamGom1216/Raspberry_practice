# 문자열 출력

import numpy as np
import cv2

# color 설정
blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)

# Font 종류
fonts = [
 cv2.FONT_HERSHEY_SIMPLEX,
 cv2.FONT_HERSHEY_PLAIN,
 cv2.FONT_HERSHEY_DUPLEX,
 cv2.FONT_HERSHEY_COMPLEX,
 cv2.FONT_HERSHEY_TRIPLEX,
 cv2.FONT_HERSHEY_COMPLEX_SMALL,
 cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
 cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
 cv2.FONT_ITALIC
]

# 모두 0으로 되어 있는 빈 Canvas(검정색)
img = np.zeros((384, 384, 3), np.uint8)

# Font 그리기
for i in range(0, len(fonts)):
    point = 30, 30 + (i * 40) # 좌표의 튜플 생성
    # x축은 30으로 고정, y축은 폰트 갯수만큼 40씩 추가
    cv2.putText(img, 'PYTHON', point, fonts[i], 1, white_color, 2, cv2.LINE_AA)
    # 출력할 문자열은 파이썬
    
cv2.imshow('text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()