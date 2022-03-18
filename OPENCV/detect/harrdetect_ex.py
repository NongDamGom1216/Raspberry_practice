from harrdetect import HarrDetect
import cv2

cascade_file = "haarcascade_frontalface_default.xml"
detecter = HarrDetect(cascade_file)

image_file = "../data/face1.jpg"
image = cv2.imread(image_file)

face_list = detecter.detect(image)

if len(face_list) > 0:
    detecter.draw_rect(image, face_list)
    cv2.imwrite("facedetect-output.PNG", image)
else:
    print("no face")
