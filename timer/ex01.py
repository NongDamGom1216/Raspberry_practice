import threading

def do_something():
    print('time out')

timer = threading.Timer(2, do_something)
timer.start()

print("main thread exit")