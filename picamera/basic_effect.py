# 카메라 이펙트 종류를 5초 간격으로 보여줌

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
   camera.image_effect = effect
   camera.annotate_text = "Effect: %s" % effect
   sleep(5)

camera.stop_preview()