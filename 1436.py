def check(num):
    return '666' in str(num)

N = int(input())

cnt = 1
start_num = 666

while cnt < N:
    start_num += 1
    if check(start_num):
        cnt += 1

print(start_num)