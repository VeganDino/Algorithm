# 바이러스
# https://www.acmicpc.net/problem/2606

n,m=int(input()), int(input())
graph=[[]*n for i in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
visited=[False]*(n+1)
def dfs(start):
    global cnt
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)