# 실버2
# 창고 다각형
import sys
input = sys.stdin.readline
n = int(input())
doong = [list(map(int, input().split())) for _ in range(n)]
doong.sort(key=lambda x : x[0])
doong_y = sorted(doong, key=lambda x: x[1])
max_height_y = doong_y[n-1][1]
max_height_x = doong_y[n-1][0]
max_height_index = doong.index([max_height_x, max_height_y])
changgo = 0

tmp = [doong[0][0], doong[0][1]]
for i in range(1, max_height_index+1):
    if tmp[1] <= doong[i][1]:
        changgo += (doong[i][0] - tmp[0]) * tmp[1]
        tmp = [doong[i][0], doong[i][1]]
tmp = [doong[n-1][0], doong[n-1][1]]
for i in range(n-2, max_height_index-1, -1):
    if tmp[1] <= doong[i][1]:
        changgo += (tmp[0] - doong[i][0]) * tmp[1]
        tmp = [doong[i][0], doong[i][1]]

changgo += max_height_y    
print(changgo)
