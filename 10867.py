N = int(input())

num_list = list(map(int, input().split()))

for num in sorted(list(set(num_list))):
    print(num, end=" ")