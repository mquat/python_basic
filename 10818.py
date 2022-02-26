#최소, 최대 

N = int(input())
x = list(map(int,input().split()))  #list로 만들어주는게 핵심 -> 그래야 max, min, sort 등의 함수를 사용할 수 있음 sum도 마찬가지. sum은 리스트 내 모든 수를 합치는 함수 
print(min(x), end=" ")
print(max(x))

#2번째 방법 
#x.sort()
#print(x[0], x[len(x)-1])