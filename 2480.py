#주사위 세개

#내가 푼 버전 
a,b,c=map(int,input().split())

if a==b==c:
    print(10000+a*1000)
else:
    if a==b or a==c:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    else:
        print(max(a,b,c)*100)


#추가 버전 (set을 이용)
x =list(map(int,input().split()))
lst = list(set(x))

if len(lst) ==1:
    print(10000+lst[0]*1000)
elif len(lst) ==2:
    for i in lst: 
        if x.count(i)==2:
            print(1000+i*100)
elif len(lst) ==3:
    print(max(lst)*100)
