from gpiozero import LED, Button
from signal import pause

led = LED(16)
button = Button(21)

led.source = button # 레벨 트리거 동작

pause()