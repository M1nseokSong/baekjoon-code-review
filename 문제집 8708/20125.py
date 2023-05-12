# 실버4
# 쿠키의 신체 측정
import sys
input = sys.stdin.readline
n = int(input())
cookie = [input().rstrip() for i in range(n)]
body = []
left_arm, right_arm, center, left_foot, right_foot = 0, 0, 0, 0, 0
for row in range(n):
    for col in range(n):
        if cookie[row][col] == "*":
            body.append([row, col])
head = [body[0][0], body[0][1]]
heart = [body[0][0]+1, body[0][1]]
for i in body:
    if i[0] == heart[0] and i[1] < heart[1]:
        left_arm += 1
    elif i[0] == heart[0] and i[1] > heart[1]:
        right_arm += 1
    elif i[0] > heart[0] and i[1] == heart[1]:
        center += 1
    elif i[0] > heart[0] and i[1] == heart[1] - 1:
        left_foot += 1
    elif i[0] > heart[0] and i[1] == heart[1] + 1:
        right_foot += 1
    
print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, center, left_foot, right_foot)

