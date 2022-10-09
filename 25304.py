std_price = int(input())
total_count = int(input())


total_price = 0
for i in range(total_count):
    price, cnt = map(int,input().split())
    total_price += price * cnt

if total_price == std_price:
    print('Yes')
else:
    print('No')

