#튜플(tuple): 속도는 list 보다 빠르나, 추가/변경 등은 불가능 

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") -> Error: tuple has no attribution 'add' 

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

#위 내용을 튜플화 
(name, age, hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)


#집합 (set), 중복 안됨 / 순서 없음 
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호","양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python 개발자 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

#합집합 (java 혹은 python 개발자 할 수 있는 사람)
print(java | python)
print(java.union(python))

#차집합 (java는 할 줄 알지만 python은 모르는 개발자)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹은 사람이 생겼어요 
java.remove("김태호")
print(java)