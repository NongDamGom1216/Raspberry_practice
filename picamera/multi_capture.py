from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate=30) # 1초에 30장

camera.iso = 100
sleep(2)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

# 고정된 설정으로 여러 사진 찍기
camera.capture_sequence(['image%02d.jpg' % i for i in range(5)])
# 리스트 컴프리헨션 사용 -> for 문이 도는 만큼 image 생성