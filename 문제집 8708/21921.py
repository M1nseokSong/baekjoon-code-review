# 실버3
# 블로그
import sys
from collections import deque
input = sys.stdin.readline
n, x = map(int, input().split())
visitor = list(map(int, input().split()))
def blog():
    cumul_sum, day = sum(visitor[:x]), 0
    visit = []
    for i, many in enumerate(visitor, start=1):
        if i >= x:
            visit.append(cumul_sum)
            if i == n:
                break
            cumul_sum -= visitor[day]
            day += 1
            cumul_sum += visitor[i]
    max_visit = max(visit)
    if max_visit == 0:
        print("SAD")
        return 
    print(max_visit)
    print(visit.count(max_visit))
    return 

blog()
