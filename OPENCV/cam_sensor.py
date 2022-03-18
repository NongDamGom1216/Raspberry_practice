# 모션 센서(pir 센서)를 이용해서
# 동작이 감지되면 녹화 시작
# 동작이 사라지면 녹화 중지

# 녹화된 동영상 파일을 서버로 업로드함

from cam import Camera, VideoRecorder
from gpiozero import MotionSensor
from openapi import upload
import cv2
from datetime import datetime

pir = MotionSensor(18)
cam = Camera(0)
recorder = VideoRecorder()

url = 'http://172.30.1.21:8000/api/upload_record/'

def stop_record(): 
    # stop 시에 여러 작업을 해야 함으로 함수 생성
    file_path = recorder.stop()

    result = upload(url, file_path)

    if result:
        print('upload success')
    else:  
        print('upload fail')


pir.when_motion = recorder.start # () 안들어감
pir.when_no_motion = stop_record


def callback(frame, key):

    # 우측 상단에 현재 날짜, 시간을 출력, 녹화 파일에도 출력
    start = datetime.now()
    now = start.strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, now, (450,20), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2, cv2.LINE_AA)

    recorder.write(frame)

    if recorder.state:
        # 녹화 시작 시 텍스트 뜨게 하기
        cv2.putText(frame, 'recording', (10, 40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2, cv2.LINE_AA)

    return True

cam.callback = callback
cam.run()