# DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque

n,m,v=map(int,input().split())
graph=[[]*n for i in range(n+1)]

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)
def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)
dfs(v)
print()

visited=[False]*(n+1)
def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        pop=q.popleft()
        print(pop, end=' ')
        for i in sorted(graph[pop]):
            if not visited[i]:
                q.append(i)
                visited[i]=True
bfs(v)