# 시험 감독
# https://www.acmicpc.net/problem/13458

n=int(input())
m=list(map(int, input().split()))
b,c=map(int, input().split())
cnt=0

for i in m:
    if i>b:
        if (i-b)%c==0:
            cnt+=(i-b)//c + 1
        else: cnt+=(i-b)//c + 2
    else: cnt+=1
print(cnt)
