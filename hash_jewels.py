#J는 보석이며, S는 돌이다. S에는 보석이 몇 개 있을까? (대소문자는 구분된다)
#결과: 3 
J = 'aA'
S = 'aAAbbbb'


from collections import Counter


#1번째 방식 
new_S  = Counter(S)
result = [new_S[J[i]] for i in range(0, len(J))]

print(sum(result))


#2번째 방식 
def Jewels(J, S):
    new_S = Counter(S)
    result = 0 

    for j in J:
        result += new_S[j]

    return result

print(Jewels(J,S))


#3번째 방식 (가장 빠름)
def Jewels(J, S):
    return sum(s in J for s in S)

print(Jewels(J,S))