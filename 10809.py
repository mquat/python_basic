#알파벳 찾기
answer = input()

for code in range(97,123):
    if chr(code) in answer:
        print(answer.index(chr(code)))

    else:
        print(-1)