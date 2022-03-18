# PIR 센서
import RPi.GPIO as GPIO
import time
# 초록색 LED, 빨간색 LED, 센서 입력핀 번호 설정
led_R = 20
led_G = 16
sensor = 12
GPIO.setmode(GPIO.BCM)
# LED 핀의 IN/OUT(입력/출력) 설정
GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_G, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)
print ("PIR Ready . . . . ")
time.sleep(5) # PIR 센서 준비 시간


# 레벨 트리거 방식(보안 카메라는 엣지 트리거 방식을 사용해야한다)
try:
    while True:
        if GPIO.input(sensor)==1: # 센서가High(1)출력
            GPIO.output(led_G, 1) # 노란색 LED 켬
            GPIO.output(led_R, 0) # 빨간색 LED 끔
            print("Motion Detected !")
            time.sleep(0.2)

        if GPIO.input(sensor) == 0: #센서가 Low(0)출력
            GPIO.output(led_R, 1)
            GPIO.output(led_G, 0)
            time.sleep(0.2)
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()

