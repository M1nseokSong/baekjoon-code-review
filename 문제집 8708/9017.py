# 실버4
# 크로스 컨트리
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    ranking = list(map(int, input().split()))
    real_ranking = list()
    team = [0]*201
    real_team = list()
    score = [[] for _ in range(201)]
    rank_4th_team = []
    for i in ranking: 
        team[i] += 1
    for i in range(len(team)):
        if team[i] == 6:
            real_team.append(i) # 6명 넘는 팀 번호들
    set_real_team = set(real_team)
    for i in range(len(ranking)):
        if ranking[i] in set_real_team:
            real_ranking.append(ranking[i]) #ranking[i]가 팀. 점수는 append된 순서대로 +1해서
    for i, team in enumerate(real_ranking):
        score[team].append(i+1)
    for i, team_score in enumerate(score):
        if len(team_score) == 6:
            rank_4th_team.append([sum(team_score[:4]), team_score[4], i])
    rank_4th_team.sort(key=lambda x : (x[0], x[1]))
    print(rank_4th_team[0][2])
