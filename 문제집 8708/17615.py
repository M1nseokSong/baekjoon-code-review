# 실버1
# 볼 모으기
import sys
input = sys.stdin.readline
n = int(input())
balls = input().strip()

cnt_list = []

def PARSE(s):
    parse_ball = balls.lstrip(s)
    cnt_list.append(parse_ball.count(s))
    parse_ball = balls.rstrip(s)
    cnt_list.append(parse_ball.count(s))

PARSE('R')
PARSE('B')

print(min(cnt_list))
