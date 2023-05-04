# 브론즈 2
# 벌집
n = int(input())
def acc(n):
    if n == 1:
        return 1
    level = 2
    x = 1
    while(True):
        if level <= n < level + 6*x:
            return x+1
        level += 6*x 
        x+=1
print(acc(n))
