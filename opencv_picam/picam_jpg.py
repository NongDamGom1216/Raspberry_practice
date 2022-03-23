# jpg 이미지를 얻어서 네트워크로 전송할 예정
# 캡쳐한 이미지는 화면에 보여주지 않음

from picamera import PiCamera
import numpy as np
import cv2
from time import sleep
from io import BytesIO

stream = BytesIO()
camera = PiCamera()

while True:
    camera.capture(stream, format='jpeg', use_video_port=True)
    data = stream.getvalue() #BytesIO의 전체 데이터 배열 얻기
    # data를 전송
    stream.seek(0) # write 시작 위치를 처음으로 보내고(파일 포인터)
    # 그리고 기존에 썼던 데이터 메모리를 비워줘야함
    stream.truncate() # 현재 위치를 기반으로 뒷 부분을 잘라내는 것(읽기 쓰기 위치 기준)
