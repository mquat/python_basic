#traceback.format_exc() : 오류 추적 결과를 문자열로 반환

import traceback

def test():
    return 10/0

def call_test():
    test()

def main():
    try:
        call_test()
    except:
        print('error occured!')
        print(traceback.format_exc())


main()