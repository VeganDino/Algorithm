# 우유 축제
# https://www.acmicpc.net/problem/14720

from collections import deque

n=int(input())
milk=list(map(int, input().split()))
lst=deque([0,1,2])
cnt=0

for i in milk:
    if i==lst[0]:
        cnt+=1
        lst.rotate(-1)
print(cnt)