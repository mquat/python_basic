#그룹 단어 체커


N = int(input())
for i in range(N):
    answer = input()
    if list(answer) != sorted(answer,key=answer.find):    #문자를 같은 문자형끼리 정렬 
        N -=1 

print(N)
