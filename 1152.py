#단어의 개수

word = input().strip()

cnt = 0 
for i in range(len(word)):
    if word[i] == " ":
        cnt += 1

if len(word)==0:
    print(cnt)
else:
    print(cnt+1)