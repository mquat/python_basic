#설탕 배달

N = int(input())
cnt_five = 0
cnt_three = 0

while N >0:
    if N%5 ==0:
        cnt_five = N//5
        break
    else:
        N -= 3
        cnt_three += 1
        if N <= 0: break

if N %5 == 0: 
    print(cnt_five+cnt_three)
else:
    print(-1)


