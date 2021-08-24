# 최소공배수
# https://www.acmicpc.net/problem/1934

t=int(input())

def lcm(x,y):
    a=x*y
    while y:
        x,y=y,x%y
    return a//x

for i in range(t):
    n,m=map(int, input().split())
    print(lcm(n,m))



