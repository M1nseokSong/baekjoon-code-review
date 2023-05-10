# 실버5
# 비밀번호 발음하기
import sys
conso = ['a', 'i', 'o', 'u', 'e']
input = sys.stdin.readline
while(True):
    cond_1, cond_2, cond_2_1, cond_2_2, cond_3 = 0, 1, 0, 0, 1
    passwd = input().strip()
    tmp = '?'
    result = 'acceptable.'
    if passwd == "end":
        break
    for i in passwd:
        if i in conso: # 모음일 때
            cond_1 += 1 # 조건 1
            cond_2_1 = 0
            cond_2_2 += 1
        else: # 자음일 때
            cond_2_1 += 1
            cond_2_2 = 0

        if tmp == i and tmp not in ['e', 'o']: # 조건 3
            cond_3 = 0
            break
        
        if cond_2_1 == 3 or cond_2_2 == 3: # 조건 2
            cond_2 = 0
            break
        tmp = i
    if cond_1 > 0 and cond_2 == 1 and cond_3 ==1:
        result = 'acceptable.'
    else:
        result = 'not acceptable.'
    print(f"<{passwd}> is {result}")
