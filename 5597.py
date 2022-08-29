num = [n for n in range(1,31)]
new_num = []
for i in range(28):
    x = int(input())
    if x in num:
        num.remove(x)

for i in num:
    print(i)