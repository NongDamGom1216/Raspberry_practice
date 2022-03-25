# 20초 뒤에 타이머에 의해 비디오 중지
# sudo apt -y install gpac
# MP4Box -add my_video.h264 my_video.mp4

import picamera
from threading import Timer

from os import path
import subprocess

camera = picamera.PiCamera()
camera.resolution = (640, 480)

def convert_to_mp4(src):
    dst = path.splitext(src)[0] + '.mp4'
    cmd = f"MP4Box -add '{src}' '{dst}'"
    # 대소문자 구분
    # subprocess.run(cmd, shell = True, stderr=subprocess.DEVNULL) # 코드 간편화
    result = subprocess.run(cmd, shell = True)
    # subprocess는 정의한 명령어를 운영체제한테 명령하도록 한다
    return not result.returncode, dst
    # 첫 번째 요소는 성공 여부에 대한 true, false

def stop_recoding():
    camera.stop_recording()
    result, dst = convert_to_mp4('my_video.h264')
    if result:
        print(dst)
    else:
        print(dst, '변환 실패')

camera.start_recording('my_video.h264')
Timer(5, stop_recoding).start()
