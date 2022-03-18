from gpiozero import LED
from signal import pause # 리눅스 파이썬에만 있다

red = LED(20)
# 스레드로 동작한다.
red.blink(on_time=0.5, off_time=0.5)
# red.blink(background=False)
# background = False를 매개변수로 넣으면 print를 못한다.(메인 스레드로 루프 돌기 때문에)

print("히나나")
pause()
# pause()랑 아래 함수랑 같은 동작
# while True:
#     pass
# 이 무한루프는 CPU가 직접 한다.(busy waiting)

# pause() -> CPU가 아닌 다른 스레드로 동작(신호가 올때까지)