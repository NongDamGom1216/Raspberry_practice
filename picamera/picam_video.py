# 20초 뒤에 타이머에 의해 비디오 중지
# sudo apt -y install gpac
# MP4Box -add my_video.h264 my_video.mp4

import picamera
from threading import Timer

camera = picamera.PiCamera()
camera.resolution = (640, 480)

def stop_recoding():
    camera.stop_recording()

camera.start_recording('my_video.h264')
Timer(20, stop_recoding).start()
