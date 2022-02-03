#list[] 배열 : 순서를 갖는 객체의 집합 (중복값 가능)

#지하철 칸 별로 10명, 20명, 30명 
subway = [10,20,30]
print(subway)

#조세호 씨가 몇 번째 칸에 타고 있는가? 
subway = ["유재석","조세호","하하"]
print(subway.index("조세호"))

#송지효씨가 다음 정류장에서 탐 
subway.append("송지효")
print(subway)

#정형돈씨를 유재석씨와 조세호씨 사이에 탑승시킴 
subway.insert(1,"정형돈")
print(subway)


#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)


#같은 이름의 사람이 몇 명 있는지 확인 
subway.append("유재석")
print(subway.count("유재석"))

#정렬 (오름차순)
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#정렬 (내림차순)
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용 
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장 (합치기)
num_list.extend(mix_list)
print(num_list)