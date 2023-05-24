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

-------- 팀원 풀이 (사람 중심이 아니라 햄버거, 사람을 쌍으로 봄)
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
PH = list(input()) # Person or Hamburger

ans = 0
for i in range(len(PH)):
    if PH[i] == 'X': # 먹은 햄버거와 먹은 사람에는 임의로 'X'를 할당한다.
        continue
    
    for j in range(i+1, min(i+K+1, len(PH))):
        if (PH[i] == 'P' and PH[j] == 'H') or (PH[i] == 'H' and PH[j] == 'P'):
            PH[i] = PH[j] = 'X'
            ans += 1
            break

print(ans)
