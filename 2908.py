#상수

answer = list(map(int,input().split()))

lst_a = str(answer[0])
lst_a = int(lst_a[2]+lst_a[1]+lst_a[0])
lst_b = str(answer[1])
lst_b = int(lst_b[2]+lst_b[1]+lst_b[0])

if lst_a - lst_b >0: print(lst_a)
else: print(lst_b)



