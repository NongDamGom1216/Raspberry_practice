from gpiozero import PWMLED
from time import sleep
from signal import pause

led = PWMLED(16)

# while True:
#     # 여기서 value는 함수(property - getter, setter)
#     led.value = 0 # off
#     sleep(1)
#     led.value = 0.5 # half brightness
#     sleep(1)
#     led.value = 1 # full brightness
#     sleep(1)

led.pulse()
pause() # 다른 스레드로 동작한다.