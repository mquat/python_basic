N = int(input())

myList = []
for _ in range(N):
    myList.append(list(map(int, input().split())))

#x[1]만 Key로 정의했더니, error // x[1],x[0]도 같이 정의해줘야 통과 
myList.sort(key=lambda x: (x[1],x[0]))

result = []
for x in myList:
    if not result or x[0] >= result[-1][1]:
        result.append(x)

print(len(result))
