# 실버2
# 랭킹전 대기열
import sys
input = sys.stdin.readline
p, m = map(int, input().split())
player = [list(input().split()) for _ in range(p)]
room_host = [] # room_host = [방장 점수]
room = [] # room = [ [ [점수, 이름], [점수, 이름] ], [  ] ]
for p in player:
    if not room_host: # 아무 방도 없으면
        room_host.append(int(p[0]))
        room.append([[int(p[0]), p[1]]])
    else: # 개설된 방이 하나라도 있으면
        tmp = 0
        for h, r in zip(room_host, room): # 개설된 모든 방 탐색
            if (len(r) < m) and (h-10 <= int(p[0]) <= h+10):
                r.append([int(p[0]), p[1]])
                tmp = 1
                break
        if tmp == 0: # 내가 들어갈 방이 없거나, 모든 방이 꽉찼으면
            room_host.append(int(p[0]))
            room.append([[int(p[0]), p[1]]])

for i in range(len(room)):
    if len(room[i]) == m:
        print("Started!")
        room[i].sort(key=lambda x : x[1])
        for j in room[i]:
            print(*j)
    else:
        print("Waiting!")
        room[i].sort(key=lambda x : x[1])
        for j in room[i]:
            print(*j)
