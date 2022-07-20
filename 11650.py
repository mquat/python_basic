N = int(input())
location = []
for _ in range(N):
    X,Y = input().split()
    location.append((int(X),int(Y)))

location.sort(key=lambda x: (x[0],x[1]))

for n in location:
    print(n[0],n[1])