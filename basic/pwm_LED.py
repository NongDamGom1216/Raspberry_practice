import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO 16번 핀을 출력으로 설정
GPIO.setup(16, GPIO.OUT)
# PWM 인스턴스 p를 만들고 GPIO 13번을 PWM 핀으로 설정, 주파수 = 50Hz

p = GPIO.PWM(16, 50)
p.start(0) # PWM 시작 , 듀티비 = 0

try:
    while 1:
        for dc in range(0, 101, 5): # dc의 값은 0에서 100까지 5만큼 증가
            p.ChangeDutyCycle(dc) # dc의 값으로 듀티비 변경
            time.sleep(0.1)

        for dc in range(100, -1, -5): # dc의 값은 100에서 0까지 5만큼 감소
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()