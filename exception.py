#예외 처리
def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0: 
        #함수 내부에는 Exception을 처리하는 except문이 없음. 따라서 상위 코드 블럭으로 넘겨짐(이 때, 상위 코드 블럭은 three_multiple()이 있는 try/except구문)
        raise Exception('3의 배수가 아닙니다.')
    print(x)

try:
    three_multiple()
except Exception as e:
    #three_multiple() 내부에서 raise된 예외가 넘겨져 해당 except문에서 처리됨. 
    #이 때, 함수 내부 Exception에 담겨진 에러메세지가 except Exception as e의 e에 담겨짐
    print('스크립트 파일에서 예외가 발생했습니다.', e)


#예외를 re-raise하기 
def three_multiple():
    try: 
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        #Exception에 넣은 에러메세지가 except Exception as e의 e에 들어감 
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise   #현재 발생한 예외를 re-raise하여 상위 코드 블럭으로 넘긴다

try: 
    three_multiple()
except Exception as e:
    #three_multiple() 내부에서 re-raise했기 때문에, 바깥에서 다시 예외처리됨 
    print('스크립트 파일에서 예외가 발생했습니다.', e)