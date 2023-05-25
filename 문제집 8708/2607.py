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

#----------------- <팀원 풀이> -----------------------------#
# 풀이 1.
def is_similar(long_word, short_word):
    long_arr = list(long_word)
    short_arr = list(short_word)

    while short_arr:
        ch = short_arr.pop()
        if ch in long_arr:
            long_arr.remove(ch)

    # long_arr의 남은 길이가 1 이하면 비슷한 단어다.
    if len(long_arr) <= 1:
        return True
    else:
        return False

def main():
    N = int(input()) # 단어의 개수
    word = input()
    
    ans = 0 # 비슷한 단어 개수
    for _ in range(N-1): # word 제외
        other = input()
        if len(word) >= len(other):
            ans += is_similar(word, other)
        else:
            ans += is_similar(other, word)
    
    print(ans)
main()
