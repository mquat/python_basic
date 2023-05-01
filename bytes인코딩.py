x = '안녕'.encode('utf-8')

print(x)
print(x.decode('utf-8'))

y = '안녕'.encode('euc-kr')
print(y)
print(y.decode('euc-kr'))

z = bytes('안녕', encoding='euc-kr')
print(z)

q = bytearray('안녕', encoding='cp949')
print(q)

print('안녕'.encode())

