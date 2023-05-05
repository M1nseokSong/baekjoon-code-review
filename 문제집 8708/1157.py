# 브론즈1
# 단어 공부
# 처음 풀이
from collections import Counter
import sys
input = sys.stdin.readline
word = input().rstrip().upper()
count_word = dict(Counter(word))
count_word = sorted(count_word.items(), reverse=True, key=lambda x:x[1])
if len(count_word) == 1:
    result = count_word[0][0]
else:
    if count_word[0][1] != count_word[1][1]:
        result = count_word[0][0]
    else:
        result = "?"
print(result)

# 좀 더 생각해본 풀이
from collections import Counter
import sys
input = sys.stdin.readline
word = input().rstrip().upper()
count_word = Counter(word).most_common(2)
try:
    if count_word[0][1] != count_word[1][1]:
        result = count_word[0][0]
    else:
        result = "?"
except IndexError:
    result = count_word[0][0]
print(result)
