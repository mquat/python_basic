#숫자 처리 함수

print(abs(-5))  #5
print(pow(4,2)) #4^2 = 16
print(max(5,12))    #12 (최대값)
print(min(5,12))    #5 (최소값)
print(round(4.99))  #5
print(round(3.14))  #3

from math import * 
print(floor(4.99))  #4 (내림)
print(ceil(3.14))   #4 (올림)
print(sqrt(16)) #4 (제곱근)



#랜덤 함수
from random import *

print(random()) #0.0 ~ 1.0 미만의 random값 생성 
print(random()*10)  #0.0 ~ 10.0 미만의 값 생성 
print(int(random()*10)) #0~10 미만의 값 생성 
print(int(random()*10)+1 ) #1~10 미만의 값 생성


print(int(random()*45)+1)   #1~45 이하의 값 생성 
print(int(random()*45)+1)   #1~45 이하의 값 생성 
print(int(random()*45)+1)   #1~45 이하의 값 생성 

print(randrange(1,46)) #1~46 미만의 값, 즉 1~45 이하의 값 생성
print(randrange(1,46)) #1~46 미만의 값, 즉 1~45 이하의 값 생성
print(randrange(1,46)) #1~46 미만의 값, 즉 1~45 이하의 값 생성
print(randrange(1,46)) #1~46 미만의 값, 즉 1~45 이하의 값 생성


print(randint(1,45)) #1~45 이하의 값 생성
print(randint(1,45)) #1~45 이하의 값 생성
print(randint(1,45)) #1~45 이하의 값 생성


#quiz
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 ", date, "일로 선정되었습니다.") 

date = randint(4,28)
print("오프라인 스터디 날짜 : " + str(date) + "입니다.")