#최대값

#정답
lst = []
for i in range(9):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)

#오답 - 중복 list를 씌우는 바람에 [[x],[x]...]와 같은 형태가 되어 버렸다. 그렇다고 x에 list를 씌우지 않으면 x는 자료형이 정해지지 않은 상태가 되어 버림  
lst = [] 
for i in range(9):
    x = list(map(int,input().split("\n")))
    lst.append(x)

print(max(lst))
print(lst.index(max(lst))+1)