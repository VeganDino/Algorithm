# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

n=[input() for _ in range(int(input()))]
cnt=0

for i in range(len(n)):
    l=len(n[i])
    
    m=[]
    for j in range(l):
        if n[i][j] not in m:
            m.append(n[i][j])
        elif n[i][j] in m and n[i][j]==m[-1]:
            m.append(n[i][j])
        else: break
    if len(m)==l: cnt+=1
print(cnt)