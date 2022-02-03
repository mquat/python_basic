print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
print(5>10) #참 / 거짓 

#주석은 한번에 선택 후 ctrl + / 하면 일괄 주석 추가 혹은 삭제됨

#애완동물을 소개해 주세요! 
animal = "강아지"
name = "연탄이"
age = 4
hobby = "낮잠"
is_adult = age >=3

print("우리집 "+animal+" 이름은 "+name+"입니다")
#print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요") #정수 등을 문자가 포함된 print에 넣으려면 문자형으로 변환해야 함
print(name, "는 ", age, "살이고, ", hobby,"을 아주 좋아해요") #+ 대신 ,로 표시할 때는 문자열 변환 없이 사용 가능. 대신 뒤에 빈칸이 하나씩 포함되어 버림 
print(name+"이는 어른일까요?" + str(is_adult))

'''
이렇게 처리하면 
여러 문장을 한번에 주석 처리 할 수 있음 
'''


#quiz

station = "신도림"
print(station+"행 열차가 도착하고 있습니다.")
print(station, "행 열차가 도착하고 있습니다.")