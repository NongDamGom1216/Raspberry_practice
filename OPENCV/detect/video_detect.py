# 영상에서 얼굴 찾기

from cam import Camera
from harrdetect import HarrDetect

cascade_file = "haarcascade_fullbody.xml"

detecter = HarrDetect(cascade_file)
cap = Camera("../data/vtest.avi")

def callback(frame, _):
    object_list = detecter.detect(frame, minSize=(50, 50))
    if len(object_list) > 0:
        detecter.draw_rect(frame, object_list)
        # minSize는 경우에 따라 다르다
    return True

cap.callback = callback
cap.run()