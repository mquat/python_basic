N = int(input())
mylist = [int(input()) for _ in range(N)]

mylist.sort()
for num in mylist:
    print(num)