# 카메라에서 얼굴 찾기

from cam import Camera
from harrdetect import HarrDetect

cap = Camera(0)
cascade_file = "haarcascade_frontalface_default.xml"
detecter = HarrDetect(cascade_file)

def callback(frame, _):
    object_list = detecter.detect(frame)
    if len(object_list) > 0:
        detecter.draw_rect(frame, object_list)
    return True

cap.callback = callback
cap.run()