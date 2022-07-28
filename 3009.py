x = []
y = []
for _ in range(3):
    X,Y=map(int,input().split())
    x.append(X)
    y.append(Y)

a = ''
b = ''
for i in x:
    if x.count(i) == 1:
        a = i

for i in y:
    if y.count(i) == 1:
        b = i  

print(a,b)    