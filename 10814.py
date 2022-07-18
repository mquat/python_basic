N = int(input())
profile = []
for i in range(N):
    age, name = input().split()
    profile.append((int(age),name, i))

#정렬 기준: 나이 순, 나이가 같으면 입력 순
#x[2] 조건이 없어도 정답 -> sort는 '안정 정렬(stable sort)'을 지원하다고 볼 수 있음 
profile.sort(key=lambda x : (x[0], x[2]))

for p in profile:
    print(p[0],p[1])