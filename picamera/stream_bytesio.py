# 하드 디스크가 아닌 메모리에 저장

from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create an in-memory stream
my_stream = BytesIO()

camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(2)

camera.capture(my_stream, 'jpeg') # 포맷 지정 필요
# 내용을 읽기 위해 스트림을 뒤감기함(rewind)
my_stream.seek(0)

image = Image.open(my_stream)
image.show()