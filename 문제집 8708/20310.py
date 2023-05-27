# 실버3
# 타노스
import sys
input = sys.stdin.readline
s = list(input().rstrip())
count_0, count_1 = s.count('0')//2, s.count('1')//2

for i, w in enumerate(s):
    if w == '1' and count_1 != 0:
        s[i] = ''
        count_1 -= 1
    if s[-1+(-1)*i] == '0' and count_0 != 0:
        s[-1+(-1)*i] = ''
        count_0 -= 1
        
print(''.join([i for i in s if i != '']))


#----다른사람풀이---# # 리스트를 뒤집어서 index를 찾고 -를 붙힌뒤 인덱스 깔맞춤을 위해 -1 한다는 아이디어 대박! #
def solution() :
    n = list(input())
    zero = n.count('0') // 2
    one = n.count('1') // 2
    
    for _ in range(zero) :
        n.pop(-(n[::-1].index('0'))-1)
    
    for _ in range(one) :
        n.pop(n.index('1'))
    
    print(''.join(n))
    
solution()
