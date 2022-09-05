n,m = map(int, input().split())

std_num = min(n,m)

for i in range(std_num,0,-1):
    value1 = n%i
    value2 = m%i

    if value1 == 0 and value2 == 0:
        print(i)
        print(i*(n//i)*(m//i))
        break
    else:
        continue    


#math 함수 사용 방법 
import math
n,m = map(int,input().split())

print(math.gcd(n,m))
print(math.lcm(n,m))        #python 3.9부터 사용 가능 


#유클리드 호제법 - 최대공약수 구하기 
#min(n,m)이 0이라면, 0이 아닌 나머지 수를 출력하고 알고리즘 종료 
#나머지 한 수가 min(m,n)으로 나눠 떨어지면, 나머지 한 수를 출력하고 알고리즘 종료 
#그렇지 않으면, 나머지를 min(m,n)에 대입하고 두 수를 바꾼 다음 다시 나눈다 


n,m = map(int, input().split())
N,M = n,m
def gcd(n,m):
    while m > 0:
        n, m = m, n % m
    print(n)
    print(N*(M//n))     #최소공배수의 계산 원리를 생각해보면 된다 (최대공약수 * 각 수의 나머지, 즉 n * (m//최대공약수))

gcd(n, m)