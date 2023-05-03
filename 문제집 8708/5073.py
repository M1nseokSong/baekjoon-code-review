# 브론즈 3
# 삼각형과 세 변
# 내 풀이
import sys
input = sys.stdin.readline
while(True):
    triangle = list(map(int, input().split()))
    if sum(triangle) == 0:
        break
    triangle.sort(reverse=True)
    if triangle[0] >= triangle[1] + triangle[2]:
        result = "Invalid"
    else:
        if triangle[0] == triangle[1]  == triangle[2]:
            result = "Equilateral"
        elif triangle[0] == triangle[1] or triangle[1] == triangle[2]:
            result = "Isosceles"
        else:
            result = "Scalene"
    print(result)

# set()을 쓰는 참신한 방법
import sys
input = sys.stdin.readline

while(True):
    t=list(map(int,input().split()))
    t.sort(reverse=True)
    d=set(t)
    
    if sum(t)==0:
        break
    if t[0] >= t[1] + t[2]:
        result = "Invalid"
    else:
        if len(d) == 1:
            result = "Equilateral"
        elif len(d) == 2:
            result = "Isosceles"
        else:
            result = "Scalene"
    print(result)
        
