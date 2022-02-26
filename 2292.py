#벌집
#1 -> 6*1 -> 6*2 -> 6*3 -> 6*4 


N = int(input())
cnt = 1 
for i in range(1000000001):
    cnt += (i*6)
    if cnt >= N: 
        print(i+1)
        break

        
