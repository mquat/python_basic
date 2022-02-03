#문자열
from types import new_class


sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요!"
print(sentence2)

sentence3 = """  
나는 소년이고,
파이썬은 쉬워요!
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0번째 값부터 2 직전의 값까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])    #처음부터 6 직전의 값까지
print("뒤 7자리 :" + jumin[7:]) #혹은 jumin[7:], 7번째 값부터 끝까지 
print("뒤 7자리 (뒤부터) : " +jumin[-7:])
print("맨 뒷자리 : " +jumin[-1])    #맨 뒤에서 7번째부터 끝까지


#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())   #소문자로 변경 
print(python.upper())   #대문자로 변경
print(python[0].isupper())  #0번째 문자가 대문자인지? (true or false)
print(len(python))  #길이 반환
print(python.replace("Python", "Java")) #python -> java로 변경

index = python.index("n")
print(index)    #5
index = python.index("n", index + 1) #5+1, 즉 6번째 글자서부터 n을 찾아라
print(index)

print(python.find("n"))
print(python.find("Java")) #find, 없는 값일 때는 -1로 표시
#print(python.index("Java")) #index, 없을 경우 그냥 오류 내버림 

print(python.count("n"))


#문자열 포맷
# print("a" + "b")
# print("a", "b")

#방법1
print("나는 %d살입니다." %20)   # %d = 정수값
print("나는 %s을 좋아해요." %"파이썬")  # %s = 문자열 
print("Apple은 %c로 시작해요." % "A") # %c = 문자


print("나는 %s살입니다." %20)  # %s는 다 가능 
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))


#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age = 20))

#방법4 (v3.6 이상~)
age = 20
color = "빨간"

print(f"나는 {age}살이며, {color}색을 좋아해요.")   #f: 변수에 저장된 값을 불러옴 


#탈출 문자 
# \n : 줄바꿈 
# \", \' : 문장 내에서 따옴표 사용 가능 
print("백문이 불여일견 \n백견이 불여일타")

print('저는 "나도 코딩"입니다.')
print("저는 \"나도 코딩\"입니다.")
print("저는 \'나도 코딩\'입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\Nanocoding")

# \r: cursor를 맨 앞으로 이동
print("red apple \rpine")

# \b: 백스페이스 (한 글자 삭제)
print("redd\bapple")

# \t: 탭
print("red\tapple")


#quiz4
site = "http://naver.com"
new = site[7:-4] 

#my_str = site.replace("http://", "")
#my_str = my_str[:my_str.index(".")]

password = new[:3] + str(len(new)) + str(new.count("e")) +"!"
print("{0}의 비밀번호는 {1}입니다." .format(site,password))