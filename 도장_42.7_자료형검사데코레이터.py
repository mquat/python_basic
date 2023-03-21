def type_check(type1,type2):
    def real_decorator(func):
        def wrapper(a,b):
            if type(a) == type1 and type(b) == type2:
                return func(a,b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다')
        return wrapper
    return real_decorator
            

@type_check(int, int)
def add(a,b):
    return a + b


print(add(10,20))
print(add(100,200))
print(add('hello','world'))