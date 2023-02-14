x = input().split()

#tuple은 del/slice 조합을 사용할 수 없으니, 바로 slice하는 방법으로 실행
print(tuple(x)[:len(x)-5])