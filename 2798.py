
# #첫 번째 방법: for문 사용 
# N,M = map(int, input().split())
# card_list = list(map(int, input().split()))
# result = 0

# for i in range(0, N):
#     for j in range(i+1, N):
#         for z in range(i+1, N):
#             new_num = card_list[i] + card_list[j] + card_list[z]
            
#             if new_num <= M:
#                 result = max(result, new_num)

# print(result)


#2번째 방법 : combinations 사용 
# combinations(list,n): list의 요소를 가지고, n개씩 조합해서 나올 수 있는 모든 조합을 tuple로 반환
from itertools import combinations

N,M = map(int, input().split())
card_list = list(map(int, input().split()))

sum = [sum(i) for i in combinations(card_list,3) if sum(i)<=M]
print(max(sum))