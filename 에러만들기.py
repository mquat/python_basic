class NotTenMultipleError(Exception):
    def __init__(self):
        super().__init__('10의 배수가 아닙니다.')


def ten_multiple():
    try:
        n = int(input('10의 배수를 입력하세요: '))
        if n % 10 != 0:
            raise NotTenMultipleError
        print('맞습니다!')
    except Exception as e:
        print('예외가 발생했습니다: ', e)


ten_multiple()


