# 실버2
# 가희와 키워드
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
keyword_set = set()
for _ in range(n):
    keyword = input().rstrip()
    keyword_set.add(keyword)
blog_list = []
for i in range(m):
    blog_list = input().rstrip().split(",")
    for j in blog_list:
        if j in keyword_set:
            keyword_set.remove(j)
    print(len(keyword_set))
