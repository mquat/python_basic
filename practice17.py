import sys 
#print("python","java", "javascript", sep=" , ", end="?") #end: 문장의 끝 부분을 ?로 바꿔달라 (그래서 줄바꿈이 적용되지 않음)
#print("무엇이 더 재밌을까요?")
#print("python","java", file=sys.stdout)
#print("python","java", file=sys.stderr)


scores ={"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")  #ljust(): 왼쪽 정렬을 하되 (left-justify), 8개 자리수를 만든 상태에서 해라 

#은행 대기순번표 
#001, 002, 003 ...

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))    #zfill(): 값이 없는 공간은 0으로 채워줌, str화 해준 다음에 사용 가능 

answer = input("아무 값이나 입력하세요: ")  #input의 경우 항상 문자열(str) 형태가 default값임 
print(type(answer))
print("입력하신 값은 "+answer+"입니다.")

