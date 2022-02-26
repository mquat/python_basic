#A+B - 8
import sys

case = int(sys.stdin.readline().rstrip())

for i in range(case):
    A,B = map(int, input().split())
    print("Case #{0}:" .format(i+1), end=" ")
    print("{0} + {1} = {2}" .format(A,B,A+B))
