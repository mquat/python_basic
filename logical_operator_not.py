#논리 연산자에서, 조건이 여러 개 일 때 드모르간의 법칙(De Morgan's Law)를 생각하면 된다 
#한 가지 추가로 알아야 할 점은, 파이썬은 논리연산자를 사용할 때 우선순위가 있다. 
# -즉, fact1 and fact2 에서 fact1만 가지고 먼저 판단한다. fact1에서 결론이 나면 fact2로 넘어가지 않는다는 뜻.


def decision1(fact1,fact2):
    if not (fact1 and fact2):   #if not fact1 OR not fact2
        return print('False가 있습니다. 확인해주세요!')
    return print('모두 True입니다!')

def decision2(fact1,fact2):
    if not (fact1 or fact2):   #if not fact1 AND not fact2
        return print('모두 False입니다!')
    return print('True가 있습니다. 확인해주세요!')    

f1 = False
f2 = True

decision1(f1,f2) 
decision2(f1,f2) 

    