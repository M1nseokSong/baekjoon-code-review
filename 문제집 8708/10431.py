# 실버5
# 줄세우기
import sys
input = sys.stdin.readline
p = int(input())
for _ in range(1, p+1):
    key = [0] * 20
    result = 0
    height = list(map(int, input().split()))
    height.pop(0)
    for turn in range(20): # 몇번째 사람
        key[turn] = height[turn]
        for check in range(turn): # 맨 앞 사람부터 turn번째 사람 전 까지 turn사람 보다 키큰 사람 첫번째 찾기
            if key[check] > key[turn]:
                for change in range(turn-1, check-1, -1): # turn 바로 전 사람부터 check까지 앞으로 가면서 뒤에부터 자리 바꿔주기
                        key[change+1] = key[change]
                        result += 1
                key[check] = height[turn]
                break
#     print(*key)
    print(f"{_} {result}")
                
