#파일 입출력
score_file = open("score.txt", "w", encoding="utf8")    #w: 쓰기 모드
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file2 = open("score.txt", "a", encoding="utf8")   #a: 덮어쓰기 모드 (append)
score_file2.write("과학 : 80")
score_file2.write("\n코딩 : 100")
score_file2.close()

score_file = open("score.txt", "r", encoding="utf8")    #r: 파일 읽기 모드  
print(score_file.read())
score_file.close()


#줄 별로 읽어오기(파일의 분량을 알고 있을 때)
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end="") #줄 별로 읽되, 줄바꿈 안함
print(score_file.readline()) #줄 별로 읽기, 한 줄 읽고 줄바꿈 적용 (print는 자동으로 줄바꿈이 되기 때문에, 2번 줄바꿈 적용되는 셈)
print(score_file.readline()) 
print(score_file.readline()) 
print(score_file.readline())   
score_file.close()

#파일이 몇 줄 인지 모를 때 
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()  #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
