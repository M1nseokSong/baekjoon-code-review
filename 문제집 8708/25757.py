# 실버5
# 임스와 함께하는 미니게임
import sys
input = sys.stdin.readline
n, game = input().split()
if game == 'Y':
    game = 1
elif game == 'F':
    game = 2
else:
    game = 3
name = [input() for i in range(int(n))]
print(len(set(name))//game)
