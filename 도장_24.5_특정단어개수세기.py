text = input('텍스트를 입력하세요: ').split()
print(text)
count = 0
for word in text:
    if word.strip('.,') == 'the':    #양쪽의 ,/.을 모두 제외 -> 만약 ~ the. 로 끝나는 경우 text에는 'the.'가 담긴다
        count += 1

print(count)

