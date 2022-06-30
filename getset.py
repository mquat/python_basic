#getattr(object, 'name') : object 내부의 요소(name)을 반환한다 

class sample:
    def __init__(self, x):
        self.x = x

s = sample(1)

print(getattr(s,'x'))   #s라는 객체 안에 요소 'x'가 있는가? 있다면 값 출력 




#setattr(object, 'name', value) : object에 새로운 요소(name)을 추가하고 value를 부여한다 
setattr(s,'y',10)
print(getattr(s,'y'))