from threading import Thread
import random
import time

class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.setDaemon(True)
        self.queue = queue

    def do(self, msg):
        print('Consumer Do ', msg)
        delay = random.uniform(2, 3) # 처리에 걸리는 지연 시간
        time.sleep(delay)
    
    def run(self):
        while True:
            msg = self.queue.get() # 만약 비어있으면 get
            self.do(msg)