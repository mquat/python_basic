i = 0 
while True:
    if i > 73:
        break

    if i % 10 != 3:
        i += 1
        continue

    print(i, end= ' ')
    i += 1