# 퇴사
# https://www.acmicpc.net/problem/14501

import sys

input=sys.stdin.readline
n=int(input())
graph=[[],[]]
dp=[0]*(n+1)
for _ in range(n):
    a,b=map(int, input().split())
    graph[0].append(a)
    graph[1].append(b)

for i in range(n-1,-1,-1):
    if graph[0][i]+i>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(graph[1][i]+ dp[i+graph[0][i]], dp[i+1])
        # P[i]+dp[i+T[i]]과 dp[i+1]중 큰 값을 넣어줌
        # P[i]=graph[1][i], T[i]=graph[0][i]
print(dp[0])       