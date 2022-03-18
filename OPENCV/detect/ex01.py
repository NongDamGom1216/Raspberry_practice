import cv2
from cv2.data import haarcascades
import os

# 파일은 .local/lib/python3.9/site-packages/cv2/data에 있다.
print(haarcascades)
harr_xml = os.path.join(haarcascades, 'haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier(harr_xml)

image_file = "../data/face1.jpg"
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150,150))

if len(face_list) > 0:
    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
    cv2.imwrite("facedetect-output.PNG", image)
else:
    print("no face")