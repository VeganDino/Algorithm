# 포도주 시식
# https://www.acmicpc.net/problem/2156

# pypy3 168ms python3 524ms

n=int(input())
g=[0]
for _ in range(n):
    g.append(int(input()))
dp=[0]
dp.append(g[1])

if n>1:
    dp.append(g[1]+g[2])
for i in range(3,n+1):
    ca1=dp[i-1]
    ca2=dp[i-2]+g[i]
    ca3=dp[i-3]+g[i-1]+g[i]
    dp.append(max(ca1, ca2, ca3))
print(dp[-1])