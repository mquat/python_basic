#크로아티아 알파벳
answer = input()
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

cnt = 0
for c in croatia:
    if c in answer:
        cnt += answer.count(c)
        answer = answer.replace(c,"*"*len(c))

print(len(answer)+cnt-answer.count("*"))
