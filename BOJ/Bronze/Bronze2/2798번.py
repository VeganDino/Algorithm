# 블랙잭
# https://www.acmicpc.net/problem/2798

from itertools import combinations
n,m=map(int, input().split())
arr=list(map(int, input().split()))
add=[sum(i) for i in combinations(arr,3)]
ans=0
for i in add:
    if abs(m-i)< m-ans and i<=m:
        ans=i
print(ans)
