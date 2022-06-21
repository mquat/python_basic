X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    A = X
    B = line-X+1
else:
    A = line-X+1
    B = X

#print(f'{A}/{B}')
print(A, '/', B, sep="")