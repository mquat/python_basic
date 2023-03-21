def dec1(func):
    def wrapper():
        print('dec1')
        func()
    return wrapper

def dec2(func):
    def wrapper():
        print('dec2')
        func()
    return wrapper

@dec1
@dec2
def hello():
    print('hello')

hello()