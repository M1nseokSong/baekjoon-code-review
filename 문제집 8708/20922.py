# 실버1
# 겹치는 건 싫어
#--- 반레 보고 풀어서 반례를 떠올리는 생각을 해야될듯 ---#
# 더 간단히 다시 풀어보기 투포인터긴 한데 복잡하게 푼듯
import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
array = list(map(int, input().split()))
result = []
compa_dict = defaultdict(list)
start, signal = 0, 0
while True:
    for i in range(start, n):
        compa_dict[array[i]].append(i)
        if len(compa_dict[array[i]]) > k:
            result.append(i-start)
            start = compa_dict[array[i]].pop(0) + 1  # 넘친 숫자의 맨 처음 idx + 1 부터 다시 시작
            compa_dict = defaultdict(list) # 초기화
            if i == n-1: # 끝까지 찼는데 마지막 포함해서 넘치는 경우는 마지막 앞에 idx 까지 더해줘야 됨
                result.append(i-start)
                signal = 1
            break
        if i == n-1:
            result.append(i-start+1) # 끝까지 찼는데 마지막 미포함인 경우는 끝까지 idx 더해줘야 됨
            signal = 1
    
    if signal == 1:
        break
print(max(result))
