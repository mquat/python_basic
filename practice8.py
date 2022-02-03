#자료구조의 변경 
#커피숍 
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)    
print(menu, type(menu))

menu = tuple(menu)  
print(menu, type(menu))

menu = set(menu)    
print(menu, type(menu))



#quiz
#댓글 이벤트 - 추첨을 통해 1명은 치킨 쿠폰, 3명은 커피 쿠폰 
#조건1: 총 댓글은 20명이 작성함 (id: 1~20)
#조건2: 무작위로 추첨하되 중복 불가 

from random import *
lst = range(1,21)   #이렇게만 하면 타입이 range, list의 함수를 사용할 수 없음  
lst = list(lst)

shuffle(lst)
winners = sample(lst, 4) #4명을 한번에 뽑아야 중복 id가 발생하지 않음 

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")
