def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t 나이 : {1} \t주 사용 언어: {2}" .format(name, age, main_lang))


#만약 같은 반 학생이라면, 나이/클래스명 등은 고정값으로 넣으면 더 편함 
profile("유재석")
profile("김태호")



def profile(name, age, main_lang):
    print(name, age, main_lang)

#아래와 같이 작성하면 순서를 바꿔도 문제없이 잘 출력됨
profile(age=20, name="유재석",main_lang="파이썬")
profile(name="김태호",age=25,main_lang="자바")


#가변인자
#def profile(name, age, lang1, lang2, lang3, lang4, lang5):
 #   print("이름 : {0}\t 나이 : {1}\t " .format(name, age), end=" ")
  #  print(lang1,lang2,lang3,lang4,lang5)

#그런데 누구는 언어가 2개고, 누구는 6개여서 추가해야 하는 상황이 온다면?  이 때, 가변인자를 사용하는 것
#가변인자: *(매개변수)
def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t " .format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

#profile("유재석",20,"python","java","c","c++","c#")
#profile("김태호",25,"kotiln","swift","","","")
profile("유재석",20,"python","java","c","c++","c#", "javascript")
profile("김태호",25,"kotlin","swift")