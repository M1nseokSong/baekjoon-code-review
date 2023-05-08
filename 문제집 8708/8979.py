# 실버5
# 올림픽
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
medal = [0] * n
gold, silver, bronze = 1000000, 1, 0.000001
for _ in range(n):
    t, g, s, b = map(int, input().split())
    medal[t-1] = [t, g*gold + s*silver + b*bronze]
medal.sort(reverse=True, key=lambda x: x[1])
index = [medal[i][0] for i in range(n)].index(k)
for i in range(n):
    if medal[i][1] == medal[index][1]:
        print(i+1)
        break
#--------------------------------------------------------#
# N, K = map(int, input().split())

# medals = [list(map(int, input().split())) for _ in range(N)]

# medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

# idx = [medals[i][0] for i in range(N)].index(K)

# for i in range(N):
#     if medals[idx][1:] == medals[i][1:]:
#         print(i+1)
#         break
