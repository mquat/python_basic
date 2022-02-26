#한수

N = int(input())

def solve(a):
    if a <100:
        return a 

    else: 
        cnt = 0
        for i in range(100,a+1):
            b = str(i)
            if int(b[0])-int(b[1]) == int(b[1])-int(b[2]):
                cnt += 1
        return 99 + cnt

print(solve(N))