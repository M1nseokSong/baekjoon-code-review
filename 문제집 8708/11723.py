# 실버 5
# 집합
import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    command = input().split()
    if command[0] == 'add':
        s.add(command[1])
    elif command[0] == 'remove':
        s.discard(command[1])
    elif command[0] == 'check':
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if command[1] in s:
            s.remove(command[1])
        else:
            s.add(command[1])
    elif command[0] == 'all':
        if len(s) != 20:
            for i in range(1, 21):
                s.add(str(i))
    else:
        s.clear()
