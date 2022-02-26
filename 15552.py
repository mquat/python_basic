#빠른 A+B
import sys

T = sys.stdin.readline().rstrip()

for i in range(int(T)):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    print(A+B)


#sys.stdin.readline() 
#sys(system-specific parameters and functions)는 아래와 같이 정의됨 
#sys: sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
#stdin은 standard input을 의미함. 사용자의 입력과 함께 개행문자 ("\n")도 받음 
#위에서, rstrip()을 붙인 이유는 개행문자를 없애주기 위함 