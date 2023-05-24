check_number = 4

def is_prime_number(num: int):
    if num > 1:
        is_divisible = False
        for n in range(2, num):
            if num % n == 0:
                print(f"{num} can be cleanly divided by {n}")
                is_divisible = True
                break
        if is_divisible:
            print("It is not the prime number")
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not the prime number")

is_prime_number(check_number)

