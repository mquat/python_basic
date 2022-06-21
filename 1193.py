N = int(input())

line = 1
while N>line:
    N -= line
    line += 1

if line%2 == 0:
    A = N
    B = line-N+1
else:
    A = line-N+1
    B = N

print(A, '/', B, sep="")