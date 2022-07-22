import sys

#함수 
def mean(lst,N):
    sum = 0
    for num in lst:
        sum += num
    return round(sum/N)

def median(lst, N):
    lst.sort()
    idx = N//2
    return lst[idx]

def mode(lst):
    # new_lst = [(lst.count(num),num) for num in set(lst)] 
    
    # new_lst.sort(key=lambda x:(x[0],-x[1]), reverse=True)

    # if len(new_lst) > 1 and new_lst[0][0] == new_lst[1][0]:
    #     return max(new_lst[0][1],new_lst[1][1])
    # else:
    #     return new_lst[0][1]

    cnt = [[0]*2 for _ in range(8001)]
    for n in lst:
        cnt[n][0] = n
        cnt[n][1] += 1

    cnt.sort(key=lambda x:(-x[1],x[0]))
    if cnt[0][1] == cnt[1][1]:
        return cnt[1][0]
    else:
        return cnt[0][0]

def gap(lst):
    lst.sort()
    return lst[-1]-lst[0]


#출력 
N = int(sys.stdin.readline())

mylist = [int(sys.stdin.readline()) for _ in range(N)]

print(mean(mylist,N))
print(median(mylist,N))
print(mode(mylist))
print(gap(mylist))