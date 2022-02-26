#곱셈

a = int(input())    #입력한 내용을 int(정수)로 변환 
b = input()     #입력한 내용 그대로 (문자열)

print(a*int(b[2]))  #b의 각 문자를 int로 변환
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b[2])+(a*int(b[1]))*10+(a*int(b[0]))*100)


