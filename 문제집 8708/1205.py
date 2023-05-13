# 실버4
# 등수 구하기
import sys
input = sys.stdin.readline
n, taesoo, p = map(int, input().split())
result = 1
if n == 0:
    pass
else:
    ranking = list(map(int, input().split()))
    if p != n:
        for _ in range(p-n):
            ranking.append(-1)

    for i in range(p):
        if i == p-1 and ranking[i] >= taesoo:
            result = -1
            break
        elif ranking[i] > taesoo and ranking[i+1] == -1:
            result += 1
            break
        elif ranking[i] == taesoo and ranking[i+1] == -1:
            break
        if ranking[i] > taesoo:
            result += 1
        elif ranking[i] < taesoo:
            break

print(result)
