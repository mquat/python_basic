files = input().split()

# print(list(map(lambda x: f'00{x}' if len(x.split('.')[0]) == 1 else f'0{x}' if len(x.split('.')[0]) == 2 else f'{x}',files)))
print(list(map(lambda x: '{0:03d}'.format(int(x.split('.')[0])) + '.' + x.split('.')[1], files)))
