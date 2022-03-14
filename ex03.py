# 녹화 기능

import cv2
from datetime import date, datetime

cap = cv2.VideoCapture(2)  # 카메라
cap = cv2.VideoCapture("http://172.30.1.12:4747/video")

frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
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

while True:
    retval, frame = cap.read()
    if not retval: break

    if vwriter:
        vwriter.write(frame)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(50)
    if key == ord('r'):
        start_record()
    elif key == ord('s'):
        stop_record()

    # 센서 연계 -> pir 센서
    # HIGH, LOW 변경시 start_record, stop_record
    
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()