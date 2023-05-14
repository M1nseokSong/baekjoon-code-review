# 스위치 켜고 끄기
# 실버 4
import sys
input = sys.stdin.readline
switch_count = int(input()) # 스위치 개수 100 이하
switch_first = [2] + list(map(int, input().split())) # 1 on 0 off
student_count = int(input()) # 학생 수 100 이하
student = [list(map(int ,input().split())) for _ in range(student_count)]
for _ in range(student_count):
    if student[_][0] == 1 : # 남자
        for i in range(student[_][1], switch_count+1, student[_][1]):
            if switch_first[i] == 0:
                switch_first[i] = 1
            else:
                switch_first[i] = 0
    else: # 여자
        left_right = 0 # 좌우 몇칸 갔는지 담는 변수
        while(True):
            if student[_][1]-left_right == 0 or student[_][1]+left_right == switch_count+1: # 스위치가 양 끝 이면 스위치 개수 짝수니 패스
                break
            if switch_first[student[_][1]-left_right] == switch_first[student[_][1]+left_right]:
                left_right += 1
            else:
                break
        left_right -= 1
        for i in range(student[_][1]-left_right, student[_][1]+left_right+1):
            if switch_first[i] == 0:
                switch_first[i] = 1
            else:
                switch_first[i] = 0

for i in range(1, switch_count+1):
    if i%20==0:
        print(switch_first[i])
    else:
        print(switch_first[i], end=' ')
