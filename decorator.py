import time


def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)    # 기존 함수를 수행, 전달받은 args/kwargs로 함수 수행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result  # 기존 함수의 수행 결과를 리턴
    return wrapper


@elapsed
def myfunc():
    print("함수가 실행됩니다.")

@elapsed
def mymsg(msg):
    print("%s를 출력합니다" %msg)

myfunc()
mymsg("I need python") 
