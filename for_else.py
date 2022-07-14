#for - else문 : for문이 '완전히' 실행됐을 경우, else문을 실행하는 구문 
#for문이 중단되는 경우: break 문에 걸린 경우 

#else문이 실행되는 경우 - 5~1까지 print한 뒤, else문 실행 
for i in range(5,0,-1):
    print(i)
else:
    print("카운트다운 완료")


#else문이 실행되지 못하는 경우 - i가 2일 때 break, 1까지 가지 못하므로 그대로 종료 
for i in range(5,0,-1):
    print(i)
    
    if i == 2: break
else:
    print("카운트다운 완료")