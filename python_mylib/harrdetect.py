import cv2
from cv2.data import haarcascades
import os

class HarrDetect:
    def __init__(self, cascade_file):
        # 현재 라즈베리에서 파일은 .local/lib/python3.9/site-packages/cv2/data에 있다.
        harr_xml = os.path.join(haarcascades, cascade_file)
        self.cascade = cv2.CascadeClassifier(harr_xml) # 분류기
    
    def detect(self, image, minSize=(150, 150)):
        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_list = self.cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=minSize)
        
        return face_list
    
    def draw_rect(self, image, face_list, color = (0 ,0, 255), thickness = 8):
        for face in face_list:
            x,y,w,h = face
            cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness)
