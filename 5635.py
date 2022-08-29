n = int(input())

total_profile = []
for _ in range(n):
    profile = input().split()
    total_profile.append(profile)

total_profile.sort(key=lambda x:(int(x[3]),int(x[2]),int(x[1])))

print(total_profile[-1][0])
print(total_profile[0][0])