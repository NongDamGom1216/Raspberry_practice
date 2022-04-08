import recorder
import kakao
import time
from gpiozero import LED, Servo

led = LED(16)
servo = Servo(23)

def FUNCTIONS():
    global audio, is_success, result
    max_time_end = time.time() + (5)
    while True:
        audio = recorder.activate() # 버튼을 누르면 녹음 시작
        is_success, result = kakao.recognize(audio)
        if time.time() > max_time_end:
            break

def main():
    while True:
        audio = recorder.activate() # 버튼을 누르면 녹음 시작
        is_success, result = kakao.recognize(audio)

        # 음성 인식 실행
        # print('인식 결과:', result['value'])

        if is_success:
            if result['value'] == '전등 켜':
                led.on()
            if result['value'] == '전등 꺼':
                led.off()
            if result['value'] == '문 열어':
                servo.max()
            if result['value'] == '문 닫아':
                servo.min()

        else:
            # 음성 합성으로 오디오 출력
            print('인식 실패:', result['value'])
            recorder.recall("<speak>다시 말씀해주세요.</speak>")


main()