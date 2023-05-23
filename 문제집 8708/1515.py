# 실버3
# 수 이어 쓰기
import sys
input = sys.stdin.readline
word = input().rstrip()
# 1027까지(102 까지만 입력가능 그럽답은 1027이겠지)
number = [] # ['1', '2', '3', --- , '1', '0', '2']
cumulative_index = 0

for i in range(1, 100000):
    for st in str(i):
        number.append(st)
number.pop() # 맨 뒤에 1027의 7 제거 # number 는 3000 index
for i in word:
    tmp = number.index(i)
    cumulative_index += (tmp + 1)
    del number[:tmp+1]

signal=0
digit = 1
result = [0, 0, 0, 0, 0, 0]
while(True):
    cumulative_index -= digit
    signal += 1
    result[digit-1] += 1
    if signal == 9 or signal == 99 or signal == 999 or signal == 9999 or signal == 99999:
        digit += 1
    if cumulative_index <= 0:
        break

# print(signal ,digit, cumulative_index)
# print(result)
print(sum(result))

