N= int(input())

def factorize(num):
    i = 2
    while num != 1: 
        if num%i == 0:
            print(i) 
            num = num/i
        elif num%i != 0:
            i += 1

#print(factorize(N)) -> facotrize 함수에 return값이 없기 때문에, print를 하면 None이 같이 출력된다. 
factorize(N)