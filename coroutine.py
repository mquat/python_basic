#coroutine, cooperative routine (여러 번 호출될 수 있고, 호출되면서 상태를 유할 수  있음)
#coroutine 또한 yield를 사용하며, yield로 값을 받아올 수 있음 
#coroutine에 값을 보내면서 코드를 실행할 때는 send(), send()가 보낸 값을 받아오려면 (yield) 형식으로 변수에 저장 

import time

#예시1 
def num_coroutine():
    while True:
        x = (yield)
        print(x)

co = num_coroutine()
next(co)    # 코루틴 안의 yield까지 코드 실행(최초 실행),  while문 안의 x = (yield)로 진입

co.send(1)  #1을 x = (yield), 즉 코루틴으로 보냄 -> print(1)
time.sleep(2)
co.send(2)  #2를 코루틴으로 보냄 -> print(2)
time.sleep(2)
co.send(3)  #3을 코루틴으로 보냄 -> print(3)


#예시 2
def coroutine_test():
    greeting = "good"
    while True:
        text = (yield greeting)
        print("text = ", end=""), print(text)
        greeting += text 

if __name__ == "__main__":
    cr = coroutine_test()
    print("cr=",end=""), print(cr)

    next(cr)
    time.sleep(2)

    print("send 1")
    print(cr.send("morning"))
    time.sleep(2)

    print("send 2")
    print(cr.send("afternoon"))
    time.sleep(2)

    print("send 3")
    print(cr.send("evening"))
    time.sleep(2)
