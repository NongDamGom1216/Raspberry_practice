# edge trigger(엣지 트리거) 주로 시용

from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")
    

def say_goodbye():
    print("Goodbye!")
    

button = Button(21, bounce_time=0.03)

# 엣지 트리거
button.when_pressed = say_hello
# say_hello()를 주면 리턴값을 배정하는 것이라서 none이 되어버림
button.when_released = say_goodbye

pause()