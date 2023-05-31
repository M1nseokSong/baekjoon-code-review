# 실버2
# 주식
# 앞에서 탐색이 뒤에서 탐색보다 더 빠른 이유가 뭘까

import sys
input = sys.stdin.readline
t = int(input())
#-----------------------------------------첫번 째 풀이(앞에서 부터 탐색) --------------------------------------------#
for _ in range(t):
    n = int(input())
    result = 0
    stock = list(map(int, input().split()))
    max_money_idx, tmp = -1, 0 
    while(True):
        max_money = max(stock[max_money_idx+1:])
        max_money_idx = n-(stock[::-1].index(max_money))-1 # 제일 뒤에 있는 max값 idx 찾기
        if max_money_idx == n-1 and tmp == max_money_idx: # 제일 끝에 왔는데 지금까지 산게 없으면 그냥 끝내기
            break
        if max_money_idx == n-1: # 제일 끝에 왔는데 지금까지 산게 남아 있으면 더하고 끝내기
            result += max_money*len(stock[tmp:max_money_idx]) - sum(stock[tmp:max_money_idx])
            break

        result += max_money*len(stock[tmp:max_money_idx]) - sum(stock[tmp:max_money_idx]) # max값 전 까지 주식으로 이득 계산
        tmp = max_money_idx+1
    print(result)
#-----------------------------------------두번 째 풀이(뒤에서 부터 탐색) --------------------------------------------#
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    max_stock = stock[-1]
    reslt = 0
    for i in range(n-2, -1, -1):
        if stock[i] <= max_stock:
            reslt += (max_stock-stock[i])
        else:
            max_stock = stock[i]
    print(reslt)
