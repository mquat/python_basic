#평균은 넘겠지 
C = int(input()) 
for i in range(C):
    scores = list(map(int,input().split()))
    n = scores.pop(0)
    average = sum(scores)/n
    cnt = 0 
    for score in scores:
        if score > average:
            cnt += 1      

    print("%.3f%%" %(cnt/n*100))









