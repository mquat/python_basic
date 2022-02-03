#dictionary: 사전, key와 value를 한 쌍으로 갖는 자료형 
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) -> 없는 값, 오류 뜨고 종료 
print(cabinet.get(5))   #none 으로 뜸 
print(cabinet.get(5,"사용 가능"))   #5에 해당하는 값을 찾되, 없으면 "사용 가능"으로 넣기 (추가의 개념)
print("hi")

print(3 in cabinet)
print(5 in cabinet)


#손님 시리즈
cabinet = {"a-3":"유재석","b-100":"김태호"}
print(cabinet["a-3"])

#새 손님 
print(cabinet)
cabinet["a-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["a-3"]
print(cabinet)

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#가게 영업 종료! 
cabinet.clear()
print(cabinet)