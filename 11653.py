N= int(input())

def factorize(num):
    i = 2
    while num != 1: 
        if num%i == 0:
            print(i) 
            num = num/i
        elif num%i != 0:
            i += 1
    
    return 

factorize(N)