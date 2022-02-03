#for
for waiting_no in range(5): #0,1,2,3,4를 변수 waiting_no에 넣겠다 
    print("대기번호 : {0}" .format(waiting_no))


starbucks = ["아이언맨","토르","아이엠그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다." .format(customer))


starbucks2 = ["귀요미류","경꼬"]
for vip in starbucks2:
    print("{0} 님, 주문하신 음료가 나왔습니다!" .format(vip))



#quiz 복습
#승객:1~50 순차적으로, #탑승 시간: 5~50분 사이 난수값(랜덤)
#운전기사: 5~15분 사이만 탑승, 이걸 count 해야함 
from random import *
order = 0 #탑승 승객 count 

for person in range(1,51):
    time = randrange(5,51)
    if 5<= time <= 15:
        print("[o] {0} 번째 손님 (소요 시간: {1}분" .format(person,time))
        order += 1
    else:
        print("[ ] {0} 번째 손님 (소요 시간: {1}분" .format(person,time))

print(f"총 탑승 승객: {order}분")