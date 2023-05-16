def hanoi(n, a, b, c):
    if n == 1:
        print('board', n, 'move', a, '->', c)
    else:
        hanoi(n-1, a, c, b)
        print('board', n, 'move', a, '->', c)
        hanoi(n-1, b, a, c)

hanoi(3, 'left', 'mid', 'right')

