#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104 
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환 
students = ["iron man", "thor","i am groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["iron man", "thor","i am groot"]
students = [i.upper() for i in students]
print(students)





#quiz
#당신은 택시기사입니다. 총 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프록그램을 작성하시오.
#규칙: 승객은 5~50분 사이의 탑승 시간이 있으며, 나는 5~15분 사이 소요되는 승객만 매칭 받는다. 

from random import * 
order_ok = 0

for user in range(1,51): 
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간: {1}분" .format(user, time))
        order_ok += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분" .format(user, time))

print(f"총 탑승 승객 : {order_ok} 분")

#내가 설계할 때 문제점 
#승객 번호는 1~50까지 순차적으로 찍혀야 하는데, 이 부분을 간과함 (탑승 시간과 똑같이 랜덤 번호를 주는 것으로 착각...그러니 list로 바꾸고 shuffle 하고 뻘짓) 
#변수 선언 남발, 이것도 애초에 승객번호가 순차적으로 찍혀야 한다는 점/range, randragne를 적절히 활용할 생각하지 못한 원인 
#전역변수 지역변수 구분할 수 있으면 더 좋을 듯 (탑승 승객을 count 하는 것은 for문 돌리고 나서 하는 것이고, 탑승시간 변수는 for문 안에서 돌리면 되는 것)

