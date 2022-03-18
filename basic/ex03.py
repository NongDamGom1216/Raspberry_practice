import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 21

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정 ,PULLUP 설정(버튼 눌렀을 때 LOW)
# 아두이노와는 다르게 라즈베리파이는 PULLUP 지원
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while 1: #무한반복
        # 만약 버튼핀에 LOW(0) 신호가 들어오면, "Button pushed!" 을 출력합니다.
        if GPIO.input(button_pin) == GPIO.LOW:
            print("Button pushed!")
        time.sleep(0.1) # 0.1초 딜레이
except:
    GPIO.cleanup() # GPIO 설정 초기화