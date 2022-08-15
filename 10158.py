w,h = map(int, input().split())
p,q = map(int, input().split())
time = int(input())


#첫 번째 방법 - 각 좌표값 x,y를 list화하여 인덱싱을 통해 구하기 (런타임 에러)
# list_w1 = [i for i in range(w+1)]
# list_w2 = [i for i in range(w-1,0,-1)]
# list_h1 = [j for j in range(h+1)]
# list_h2 = [j for j in range(h-1,0,-1)]

# x = list_w1 + list_w2
# y = list_h1 + list_h2

# if (p+time) < (len(x)):
#     p = x[p+time]
# else:
#     p = x[len(x)-(p+time)]

# if (q+time) < (len(y)):
#     q = y[q+time]
# else:
#     q = y[len(y)-(q+time)]

# print(p,q)

#두 번째 방법 - 현재 좌표에서 time을 더한 좌표와, 각각 w과 h로 나눈 몫과 나머지를 사용해 구하기(런타임 에러 나지 않음) 
round_w = (p+time)//w   # 몫 
round_h = (q+time)//h   # 몫  

#만약 왕복을 끝냈다면(즉 2의 배수라면), 좌표값은 나머지 
#만약 왕복이 아니라면(즉 2의 배수가 아니라면), 좌표값은 w 혹은 h - 나머지 
if round_w%2 == 0:  
    w = (p+time)%w
else:
    w = w - ((p+time)%w)

if round_h%2 == 0:
    h = (q+time)%h
else:
    h = h - ((q+time)%h)

print(w,h) 