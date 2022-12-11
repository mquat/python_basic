class myAttribute:
    a = 1
    
    def b(self):
        pass

#hasattr: b라는 멤버가 있는가? (true/false)
print(hasattr(myAttribute, 'b'))

#getattr: a라는 변수의 값 호출(1)
print(getattr(myAttribute, 'a'))

# a라는 변수에 값 9 설정하기(a=9)
setattr(myAttribute, 'a', 9)
print(myAttribute.a)

# a라는 변수를 삭제하기
delattr(myAttribute,'a')
print(hasattr(myAttribute,'a'))     #false