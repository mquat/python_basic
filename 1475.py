N = input()
mylist = [int(x) for x in N]

for i in range(0,len(N)):
    if mylist[i] == 6 and mylist.count(6) > mylist.count(9):
        mylist[i] = 9
    elif mylist[i] == 9 and mylist.count(9) > mylist.count(6):
        mylist[i] = 6

result = [mylist.count(num) for num in mylist]
print(max(result))
