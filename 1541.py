
expression = input().split('-')
calc = 0 

for e in expression[0].split('+'):
    calc += int(e)

for i in range(1,len(expression)):
    for e in expression[i].split('+'):
        calc -= int(e)

print(calc)