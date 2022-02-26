#평균

N = int(input())
score = list(map(int,input().split()))
M = max(score)

#list comprehension 활용, 덕분에 이게 append 기능을 포함하고 있다는 걸 다시 한번 알았다
new_score = [(score[i]/M)*100 for i in range(N)]
print(sum(new_score)/len(new_score))
