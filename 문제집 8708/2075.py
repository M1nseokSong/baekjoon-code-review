# 실버2
# N번째 큰 수
import sys
import heapq
input = sys.stdin.readline
n = int(input())
#------------메모리 초과---------------#
# array = [list(map(int, input().split())) for _ in range(n)]
# result = sorted(array[-1]) # [20, 32, 41, 49, 52]
# array = list(map(list, zip(*array)))
# array.sort(reverse=True, key=lambda x : x[n-1])
# for i in array:
#     for j in range(n-1, -1, -1):
#         for k in range(n-1, -1, -1):
#             if i[j] >= result[k]:
#                 result[k] = i[j]
#                 break
#         if i[j] <= result[0]:
#             break
#     if i[-1] <= result[0]:
#         break
# print(result[0])

heap = []
for _ in range(n):
    array = list(map(int, input().split()))
    for i in array:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])      
