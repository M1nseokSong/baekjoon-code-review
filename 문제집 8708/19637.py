# 실버3
# IF문 좀 대신 써줘
import sys
input = sys.stdin.readline
from bisect import bisect_left
n, m = map(int, input().split())
title_list = []
length_list = []
for i in range(n):
    name, length = input().split()
    if length_list and int(length) == length_list[-1]:
        continue
    title_list.append(name)
    length_list.append(int(length))
    
def chingho(power):
    start, end = 0, len(length_list)-1
    while(start <= end):
        mid = (start + end) // 2
        if power <= length_list[mid]:
            end = mid-1
        else:
            start = mid+1
    return title_list[start]

for i in range(m):
    power = int(input())
    print(chingho2(power))
#-------------------------------------------bisect----------------------------#
# 실버3
# IF문 좀 대신 써줘
import sys
input = sys.stdin.readline
from bisect import bisect_left
n, m = map(int, input().split())
title_list = []
length_list = []
for i in range(n):
    name, length = input().split()
    title_list.append(name)
    length_list.append(int(length))

def chingho2(power):
    return title_list[bisect_left(length_list, power)]

for i in range(m):
    power = int(input())
    print(chingho2(power))
