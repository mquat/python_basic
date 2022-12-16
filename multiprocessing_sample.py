#multiprocessing: CPU 연산 중심일 때, threading보다 효과적이다. 단, 여러 CPU가 있는 멀티코어 환경에서만 가능하다.
#(threading의 경우, 어차피 파이썬은 GIL 이 적용되어 싱글 스레드만 허락하기에 I/O bound가 아닌 CPU bound이면 그다지 효과가 없을 가능성이 크다)
import time, threading, multiprocessing

def my_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' %name)



if __name__ =='__main__':
    start = time.time()
    # threads = []
    procs = [] 

    for i in range(4):
        # t = threading.Thread(target=my_work, args=(i,))
        # t.start()
        # threads.append(t)

        p = multiprocessing.Process(target=my_work, args=(i,))
        p.start()
        procs.append(p)

    # for t in threads:
        # t.join()

    for p in procs:
        p.join()

    end = time.time()

    print(f"수행 시간: {end-start}초")