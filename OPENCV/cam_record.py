import cv2
from cam import Camera
from datetime import datetime

cam = Camera(0) 

frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fname = ''
vwriter = None # 전역 변수 vwriter

def start_record():
    global vwriter
    if vwriter: return # 이전에 r을 눌렀는데, 또 누른 경우 그냥 리턴

    start = datetime.now()
    fname = start.strftime('./data/%Y%m%d_%H%M%S.mp4')
    vwriter = cv2.VideoWriter(fname, fourcc, 20.0, frame_size)

    print('start recoding:', fname)

def stop_record():
    global vwriter
    if not vwriter: return
    
    vwriter.release()
    vwriter = None
    print('stop recording.')

def callback(frame, key):
    if key == ord('r'):
        start_record()
    elif key == ord('s'):
        stop_record()

    if vwriter:
        vwriter.write(frame)
    
    return True

cam.callback = callback
cam.run()

