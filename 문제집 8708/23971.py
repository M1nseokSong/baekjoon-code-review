# 브론즈3
# ZOAC 4
import sys
input = sys.stdin.readline
h, w, n, m = map(int, input().split())
col = (h-1) // (n+1) + 1
row = (w-1) // (m+1) + 1
print(row*col)
