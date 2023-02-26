def prime_number_generator(x,y):
    for num in range(x,y):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
            
        if is_prime is True:
            yield num

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)

for i in g:
    print(i, end=' ')