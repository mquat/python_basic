#지역변수와 전역변수 (지역변수는 특정 함수 내에서 사용되며, 함수가 끝나면 사라짐)
gun = 10

#전역변수 활용하는 방법
def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun 사용, 그런데 이런식으로 전역변수를 남용하는 것은 좋지 않음 (관리하기 용이하지 않음)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

#두 번째 방법 (gun도 매개변수로 받아야함)
def checkpoint_return(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun  #변경된 gun을 함수 바깥에서도 사용할 수 있음

print("전체 총 : {0}" .format(gun))
#checkpoint(2)
gun = checkpoint_return(gun,2)
print("남은 총: {0}" .format(gun))


#quiz
#표준 체중을 구하는 프로그램 

#gender, height, 함수 std_weight
#남자: height * height * 22
#여자: height * height * 21 


def std_weight(gender,height):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21
    
height = 175 
gender = "남자"
weight = round(std_weight(gender,height/100),2)

print("표준 몸무게: {0}cm {1}의 표준 체중은 {2}kg입니다." .format(height,gender,weight))
    

def std_weight(gender,height):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height=162
gender="여자"
weight=round(std_weight(gender,height/100),2)

print("표준 몸무게: {0}cm {1}의 표준 체중은 {2}kg입니다." .format(height,gender,weight))

