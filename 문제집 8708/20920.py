# 실버3
# 영단어 암기는 괴로워
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
word_dic = dict()
for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1
new_word_dic = sorted(word_dic.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))
for i in new_word_dic:
    print(i[0])
