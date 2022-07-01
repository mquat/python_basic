N = int(input())

words = list(set([input() for _ in range(N)]))

# words = list(set(words))
words.sort()
words.sort(key=len)

for w in words:
    print(w)
