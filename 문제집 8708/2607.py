# 실버3
# 비슷한 단어
import sys
input = sys.stdin.readline
n = int(input())
word = input().rstrip()
word_list = list(input().rstrip() for _ in range(n-1))
result = 0
for i in word_list:
    tmp = list(word)
    cnt = 0
    for j in i:
        if j in tmp:
            tmp.remove(j)
        else:
            cnt += 1
    if cnt <= 1 and len(tmp) <= 1:
        result += 1
print(result)
