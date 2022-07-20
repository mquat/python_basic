N = int(input())
location = []

#기본 풀이
for _ in range(N):
    X,Y = input().split()
    location.append([int(Y),int(X)])

location.sort() #오름차순이 default, 추가 설정 필요 없음 

for n in location:
    print(n[1],n[0])

#추가 풀이
for _ in range(N):
    X,Y = input().split()
    location.append((int(X),int(Y)))

location.sort(key=lambda x: (x[1],x[0]))

for n in location:
    print(n[0],n[1])