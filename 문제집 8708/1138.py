# 실버2
# 한 줄로 서기
import sys
input = sys.stdin.readline
n = int(input())
height = list(map(int, input().split()))
result = [0] * n
for i, h in enumerate(height):
    cnt = 0
    for idx in range(n):
        if result[idx] == 0:
            cnt += 1
        if cnt == h+1:
            result[idx] = i+1
            break
print(*result)
