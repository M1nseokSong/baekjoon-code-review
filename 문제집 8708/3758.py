# 실버3
# KCPC
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    # 팀 개수, 문제 개수, 팀 id, 로그 엔트리 개수
    n, k, t, m = map(int, input().split())
    # team = [팀번호, [점수리스트], 제출 횟수, 마지막 제출 시간]
    team = [[p+1, [0]*k, 0, 0] for p in range(n)]
    for q in range(m):
        # 팀 id, 문제 번호, 획득 점수
        i, j, s = map(int, input().split())
        if s > team[i-1][1][j-1]:
            team[i-1][1][j-1] = s
        team[i-1][2] += 1
        team[i-1][3] = q
    for i in range(n):
        team[i][1] = sum(team[i][1])
    team.sort(reverse=True, key=lambda x : (x[1], -x[2], -x[3]))
    for i in range(n):
        if team[i][0] == t:
            print(i+1)
            break
