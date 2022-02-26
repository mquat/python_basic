#숫자의 개수

a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
#list comprehension 이용 
result = [int(a) for a in str(mul)]

for i in range(10):
    print(result.count(i))
