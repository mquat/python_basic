print(1+1) #2 
print(2**3) #2^3 = 8
print(5&3) #2 (나머지)
print(5//3) #1 (몫)
print(10//3) #3

print(10>3) #True
print(4>=7) #False
print(5<=5) #True

print(1 != 3)   #True
print(not(1 !=3))   #False

print((3>0) and (3<5))  #True
print((3>0) & (3<5))    #True

print((3>0) or (3<5))   #True
print((3>0) | (3>5))    #True

print(5>4>3)    #True
print(5>4>7)    #False


#간단한 수식 
print(2+3*4)    #14
print((2+3)*4)  #20
number = 2+3*4 
print(number)

#number = number + 2    #16
number += 2
print(number)   #16

number -= 2
number *= 2
number /= 2
number %= 2 #0
print(number)
