# 실버5
# 덩치
import sys
input = sys.stdin.readline
n = int(input())
dungchi = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n):
    count = 0
    for j in range(n):
        if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            count += 1
    result.append(count+1)
print(*result)
