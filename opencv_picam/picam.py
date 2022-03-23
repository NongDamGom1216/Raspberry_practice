# opencv 객체로 캡쳐하기
import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (640, 480)

    image = np.empty((480, 640, 3), dtype=np.uint8)

    start = time.time() # 밑의 두 줄을 실행하는데 걸린 시간 계산하기

    camera.capture(image, 'bgr') # 넘파이 배열에 저장
    cv2.imshow('frame', image)

    end = time.time()

    fps = 1/(end-start)
    print(f'fps: {fps:.2}')

    cv2.waitKey(0)