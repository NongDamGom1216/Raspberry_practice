import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# GPIO 6번 핀을 출력으로 설정
GPIO.setup(26, GPIO.OUT)
# PWM 인스턴스 p를 만들고 GPIO 18번을 PWM 핀으로 설정, 주파수 = 100Hz
p = GPIO.PWM(26, 100)
# 4옥타브 도~시 , 5옥타브 도의 주파수
Frq = [ 262, 294, 330, 349, 392, 440, 493, 523 ]
speed = 0.5 # 음과 음 사이 연주시간 설정 (0.5초)

p.start(10) # PWM 시작 , 듀티사이클 10 (충분)

try:
    while 1:
        for fr in Frq:
            p.ChangeFrequency(fr) #주파수를 fr로 변경
            time.sleep(speed)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()