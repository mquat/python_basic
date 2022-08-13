#MIT opencourse - 예시로 나온 문제
# 머리 수와 다리 수가 각각 주어질 때, 돼지와 오리의 수를 구하는 함수 

def solve(heads,legs):
    #구하는 함수 구현 
    #heads = pigs + ducks 이고, legs = (4*pigs) + (2*ducks)
    #만약 pig가 1마리 일 때 오리는 7마리 (head - pig) -> (4*2) + (2*6) = 20이 성립되지 않으므로, 다른 수를 다시 찾아서 test해야 함 
    #즉, 위의 2가지 step을 모두 거쳐야 함 
    for pigs in range(1,heads+1):
        ducks = heads - pigs
        if (4*pigs) + (2*ducks) == legs:
            return(pigs, ducks)
    return None

def barnYard():
    #입력받기 (머리 수, 다리 수)
    heads = int(input("총 머리 수: "))
    legs = int(input("총 다리 수: ")) 

    #구하기 - 구하는 함수는 별도로 정의한다 
    result = solve(heads,legs)
    if result is None:
        print("구할 수 없습니다.")
    else:
        print(f"돼지 수: {result[0]}")
        print(f"오리 수: {result[1]}")

barnYard()