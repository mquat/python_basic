N = int(input())

# for _ in range(N+1):   
#     if N == 1: 
#         print('*')
#         break
#     print('*' * N)
#     N -= 1


#range의 step을 이용하는 방법
#range(startpoint,endpoint,step) - 시작숫자부터 종료숫자 바로 앞 숫자까지 컬렉션을 만들어주며, 시작숫자와 step은 생략 가능 
for i in range(N,0,-1): #만약 N이 5라면, 5-4-3-2-1까지 만들어줌 
    print('*'*i)


#range+len의 결합은 파이썬에서 별로 권장하지 않는다고 한다
s = [1,3,5]
# for i in range(len(s)):
    # print(s[i])
for i in s:
    print(i)
