# 실버3
# 햄버거 분배
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
burger = list(input().rstrip())
result = 0
for i, ham in enumerate(burger):
    if ham == 'P':
        for j in range(max(i-k, 0), min(n, i+k+1)):
            if burger[j] == 'H':
                burger[j] = 'E'
                result += 1
                break
print(result)
