# 예산3
# 실버3
import sys
input = sys.stdin.readline
n = int(input())
money = list(map(int, input().split()))
max_money = int(input())
money.sort()
def yesan(n, money, max_money):
    if sum(money) <= max_money:
        return money[-1]
    center = n//2
    ud = 1
    if sum(money[:center]) + money[center] * (n-center) > max_money:
        ud = -1
    value = money[center]
    # print(value)
    while(True):
        mid = 0
        value += ud
        for i, tmp in enumerate(money):
            if tmp > value:
                mid = i
                break
        if sum(money[:mid]) + value * (n-mid) > max_money:
            if ud == 1:
                return value -1
            elif ud == -1:
                continue
        elif sum(money[:mid]) + value * (n-mid) <= max_money:
            if ud == 1:
                continue
            else:
                return value
            



print(yesan(n, money, max_money)) 
