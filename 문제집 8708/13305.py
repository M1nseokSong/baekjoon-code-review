# 실버3
# 주유소
import sys
input = sys.stdin.readline
n = int(input()) # 도시 개수
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
before_cost = cost[0]
result = 0
for i in range(len(cost)-1):
    if cost[i] < before_cost:
        before_cost = cost[i]
    result += before_cost * road[i]
print(result)
