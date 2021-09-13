n=int(input())
graph=[]
count=[]
cnt=0
for _ in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        cnt+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            count.append(cnt)
            cnt=0

print(len(count))
for i in sorted(count):
    print(i)