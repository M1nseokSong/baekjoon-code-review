# 실버2
# DFS와 BFS
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v):
    print(str(v), end=' ')
    for i in range(1, n+1):
        if MAP[v][i] == 1 and check_dfs[i] is False:
            check_dfs[i] = True
            DFS(i)

def BFS(v):
    queue = deque([])
    queue.append(v)

    while queue:
        x = queue.popleft()
        if check_bfs[x] is False:
            check_bfs[x] = True
            print(x, end= ' ')
            for i in range(1, n+1):
                if MAP[x][i] == 1 and check_bfs[i] is False:
                    queue.append(i)

n, m, v = map(int, input().split()) # 정점, 간선 ,탐색 시작 vertex
MAP = [[0] * (n+1) for _ in range(n+1)]
check_dfs = [False] * (n+1)
check_bfs = [False] * (n+1)

for i in range(m):
    start, end = map(int, input().split())
    MAP[start][end] = 1
    MAP[end][start] = 1

check_dfs[v] = True

DFS(v)
print()
BFS(v)
