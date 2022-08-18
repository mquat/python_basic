
#알파벳이라는 dict를 만들어 key/value를 사용하는 방법
alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
S = input()

for char in S: 
    if char in alphabet.keys():
        alphabet[char] += 1
    else:
        continue

for char in alphabet:
    print(alphabet[char], end=' ')

# ord 사용 (ASCII에 따라, 'a'는 97, 'b'는 98 등이다)
S = input()
cnt = [0]*26

for char in S:
    cnt[ord(char)-97] += 1

print(*cnt)