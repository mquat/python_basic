import random

TRIAL = 10000
same_birthday = 0

for _ in range(TRIAL):

    birthdays = []
    for _ in range(23):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthday += 1
            break
        birthdays.append(birthday)

result = (same_birthday/TRIAL)*100

#결과: 최소 50% 이상 나온다 
print(f'생일이 같을 확률은: {result}% 입니다!')