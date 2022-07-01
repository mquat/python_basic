#기존 방법 (204ms) - input()은 줄바꿈('\n\')을 삭제하는 작업을 거친다 
# N = int(input())
# words = list(set([input() for _ in range(N)]))

#더 빠른 방법 (176ms) - sys.stdin.readline()은 줄바꿈을 삭제시키지 않는다 
import sys

N = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().strip() for i in range(N)]))     #readline은 '\n\'을 포팜하므로, strip()처리를 해야한다 

words.sort()
words.sort(key=len)

for w in words:
    print(w)
