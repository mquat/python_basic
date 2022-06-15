#threading 모듈 사용해보기 

import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('sub thread start', threading.currentThread().getName())
        time.sleep(3)
        print('sub thread end', threading.currentThread().getName())


print('main thread start')

for i in range(5):
    name = 'thread {}'.format(i)
    t = Worker(name)
    t.start()   #sub thread 인 t 실행(run 메소드)

print('main thread end')