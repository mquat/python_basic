from http.client import PRECONDITION_FAILED
import sys
from typing import List


# O(n) 으로 풀기. 그렇지 않으면 브루트 포스로 풀어야 하느데, 이 경우 시간복잡도가 O(n2)일 수 밖에 없다
def maxProfit(prices: List[int])->int:
    profit = 0
    min_price = sys.maxsize     #시스템의 가장 작은 값 (TypeError가 발생하지 않는다)

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)

    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))