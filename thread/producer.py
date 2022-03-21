from threading import Thread
import random
import time

class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.daemon = True
        self.queue = queue
        self.count = 0
    
    def producer(self):
        # 생산에 걸리는 지연 시간
        delay = random.uniform(0.5, 0.8) # 0.5 ~ 0.8초
        time.sleep(delay)

        self.count += 1
        msg = self.count
        print('Producer produce ', msg)
        self.queue.put(msg) # 만든 데이터를 queue에 삽입

    def run(self):
        while True:
            self.producer()