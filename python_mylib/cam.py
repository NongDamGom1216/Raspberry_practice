# mylib 사용하는법
# .bashrc에 추가
# export PYTHONPATH=/home/pi/python_mylib

import cv2
from datetime import datetime

class Camera:
    def __init__(self, src, show = True):
        self.cap = cv2.VideoCapture(src)
        self.frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.callback = None
        self.show = show

    def run(self):
        while True:
            retval, frame = self.cap.read() # 프레임 캡쳐
            if not retval : break

            key = cv2.waitKey(50)
            if key == 27: break # ESC 키를 누른 경우
            
            if self.callback:
                result = self.callback(frame, key)
                if not result: break

            if self.show : # 항상 보여주는 것은 아니기 때문에 show = True일 때만 화면을 보여준다.
                cv2.imshow('frame', frame)
                
        if self.cap.isOpened():
            self.cap.release()
        
        cv2.destroyAllWindows()

class VideoRecorder:
    def __init__(self):
        self.file_path = '' # 녹화 파일의 경로
        self.vwriter = None
        self.state = False # True: 녹화중
    
    def start(self, frame_size=(640, 480), fps=20):
        if self.state : return

        start = datetime.now()
        self.file_path = start.strftime('./data/%Y%m%d_%H%M%S.mp4')
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.vwriter = cv2.VideoWriter(self.file_path, fourcc, fps, frame_size)
        self.state = True
        print('start recoding:', self.file_path)

    def stop(self):
        if not self.state: return
        result = self.file_path

        self.vwriter.release()
        self.vwriter = None
        self.file_path = ''
        self.state = False
        print('stop recording.')
        return result

    def write(self, frame):
        if self.state:
            self.vwriter.write(frame)

        