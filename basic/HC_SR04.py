# 초음파 센서

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#센서에 연결한 Trig와 Echo 핀의 핀 번호 설정
TRIG = 24
ECHO = 23
print("Distance measurement in progress")

#Trig와 Echo 핀의 출력/입력 설정
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Trig핀의 신호를 0으로 출력
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)


try:
    while True:
        GPIO.output(TRIG, True) # Triger 핀에 펄스신호를 만들기 위해 1 출력
        time.sleep(0.00001) # 10μs 딜레이
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            start = time.time() # Echo 핀 상승 시간, ECHO가 1이 되었을 때 시작
        while GPIO.input(ECHO)==1:
            stop= time.time() # Echo 핀 하강 시간, ECHO가 0이 되었을 때 스탑
        check_time = stop - start
        distance = check_time * 34300 / 2 # 음속
        print("Distance : %.1f cm" % distance)
        time.sleep(0.4) # 0.4초 간격으로 센서 측정
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()