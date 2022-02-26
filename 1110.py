#더하기 사이클 

n = int(input()) 
new_n = n   #이걸 안넣으면 안되는게, 그냥 n을 가지고 계산해서 쭉 넣으면 나중에 비교해야 할 첫 입력값이 사라짐. 
i = 0       #그래서 new_n에 n을 넣어서 new_n에서 계속 값이 갱신되도록 만들고, new_n == n이 성립되게 해야함. 

while True:

    a = new_n//10
    b = new_n%10 
    c = (a+b)%10 
    new_n = (b*10)+c
    i += 1
    if new_n == n:
        break

print(i)
