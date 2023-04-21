prices = list(map(int, input().split(';')))

prices.sort(reverse=True)
for price in prices:
    print('{0:>9,}'.format(price))

