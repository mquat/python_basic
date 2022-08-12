#숫자 판별 시리즈

x='3'

#isdigit() - 숫자처럼 생긴 모든 str를 숫자로 판단
print(x.isdigit())

#isdecimal() - 주어진 str을 int로 반환 가능한지를 판단 (특수문자의 숫자는 숫자로 판단하지 않음)
print(x.isdecimal())

#isnumeric() - 숫자값 표현에 해당하는 문자열까지 모두 인정 (예를 들어 분수 형태도 숫자로 인정한다)
print(x.isnumeric())