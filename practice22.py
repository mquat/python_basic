#quiz
#매주 일정한 형태의 보고서 파일을 만드는 프로그램 작성 (1주차 ~ 50주차)
#파일명은 '1주차.txt', '2주차.txt' ... 와 같이 만들 것

report_no = range(1,51)
for i in report_no:
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        #report_file.write("- "+str(i)+" 주차 주간보고 -")
        #report_file.write("- {}주차 주간보고 -" .format(i))
        report_file.write("- %s주차 주간보고 - ", i)
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")

#i를 문자화(str)하는 것을 빼먹음 
#for문에서 i in range(1,51)로 바로 작성해보자 (더 간결하니까)