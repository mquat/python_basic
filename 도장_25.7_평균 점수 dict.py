maria = {'korean':94, 'english':91, 'mathematics':89, 'science':83}

## 일반적인 방법
average = sum(maria.values())/len(maria)
print(average)


## generator를 통해서 구현해봄 (generator 개념 학습용임)
def accumulate():
    average = 0
    while True:
        score = yield
        if score is None:
            return average
        average += score

def avg_coroutine():
    while True:
        total = yield from accumulate()
        print(total/len(maria))

result = avg_coroutine()
next(result)

for score in maria.values():
    result.send(score)

result.send(None)