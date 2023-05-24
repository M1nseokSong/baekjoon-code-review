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
#--------------------------------팀원 풀이 --------------------------------------------#
import sys
input = sys.stdin.readline
N, X = map(int, input().split())
num_visitors = list(map(int, input().split()))

def find_max_visitor():
    curr_sum = sum(num_visitors[:X])
    max_sum = curr_sum
    cnt = 1
    for i in range(1, N-X+1):
        curr_sum = curr_sum - num_visitors[i-1] + num_visitors[i+X-1]
        if curr_sum == max_sum:
            cnt += 1
        elif curr_sum > max_sum:
            cnt = 1
            max_sum = curr_sum

    return max_sum, cnt
    
num, cnt = find_max_visitor()
print("SAD") if num == 0 else print(f"{num}\n{cnt}")

#최대값이랑 개수 찾는 문제는 내 방식보다 팀원의 방식이 좋아보임. 속도 측면에서
