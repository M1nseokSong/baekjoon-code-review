# 실버2
# 에디터
import sys
input = sys.stdin.readline
l_stack = list(input().rstrip())
r_stack = list()
m = int(input())
for _ in range(m):
    command = list(input().split())
    if command[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif command[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif command[0] == 'B' and l_stack:
        l_stack.pop()
    elif command[0] == 'P':
        l_stack.append(command[1])

print(''.join(l_stack + r_stack[::-1]))

