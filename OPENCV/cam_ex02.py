# cam.py의 녹화기능 클래스 실행 예제

from cam import Camera, VideoRecorder
import cv2

cam = Camera(0)
recorder = VideoRecorder()

def callback(frame, key):
    if key == ord('r'):
        recorder.start()
    elif key == ord('s'):
        recorder.stop()

    recorder.write(frame)
    return True

cam.callback = callback
cam.run()