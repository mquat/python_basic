#아래 3개 함수는 모두 결과가 같은가?

import dis

def f1():
    print('hello world!')
    return None

def f2():
    print('hello world!')
    return

def f3():
    print('hello world!')

#결과는 같다 (hello world!)
f1()
f2()
f3()

print('----------------------------------------')
#dis를 적용해보자 (바이트 코드)
f1()
dis.dis(f1)
print('----------------------------------------')
f2()
dis.dis(f2)
print('----------------------------------------')
f3()
dis.dis(f3)


"""
PEP8 says, 'Be consistent in return statements.
If any return statement returns an expression, any return statements where no value is returned should explicitly state this as return None...'
"""

"""
*from stackoverflow(https://stackoverflow.com/a/15300671)

They all return None and that's it. However, there is a time and place for all of these.
1) Using 'return None'
- This tells that the function is indeed meant to return a value for later use, and in this case it returns None.
2) Using 'return'
- This is used for the same reason as break in loops...you only want to exit the whole function. 
3) Using nothing
-It simply means that the function ended successfully. (return value(None) is not meant to be used further)
"""