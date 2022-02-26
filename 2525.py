#오븐 시계
h,m = map(int,input().split())
gap = int(input())
sum = m+gap

#ver1 
if sum >=60: 
    if (h+(sum//60)) <24: 
        print("{0} {1}" .format((h+(sum//60)),sum%60))
    else:
        print("{0} {1}" .format((h+(sum//60))-24,sum%60))
else:
    print("{0} {1}" .format(h, sum))

#ver2 
h,m=map(int, input().split())
gap = int(input())

h += gap//60 
m += gap%60

if m >= 60:
    h += 1
    m -= 60
if h>=24:
    h -= 24 

print(h,m)


#ver3
h,m=map(int, input().split())
gap = int(input())
sum = h*60+m   #아예 분으로 환산해버림 
sum += gap

if sum >= 1440: sum -= 1440 #24시간 * 60 = 1440분 

print("%d %d" %(sum//60,sum%60))