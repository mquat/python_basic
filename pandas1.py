#Pandas: 데이터 조작 및 분석을 위한 Python 프로그래밍 언어 용으로 작성된 소프트웨어 라이브러리
import pandas as pd

mydataset = {
    'cars': ["BMW", "Chevy", "Benz"],
    'passings': [3, 7, 2],
    'country' : ['Germany', 'US','']
}

#계속 작동이 되지 않아 오류를 찾아보니, python version과 pandas version이 align되지 않아서라고.
#따라서, python3. [file name.py] 를 통해 run하여 오류 해결 
myvar = pd.DataFrame(mydataset)
print(myvar)