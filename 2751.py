N = int(input())
mylist = []
for _ in range(N):
    mylist.append(int(input()))

mylist.sort()

for num in mylist:
    print(num)