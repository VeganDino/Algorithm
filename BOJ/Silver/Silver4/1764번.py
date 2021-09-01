# 듣보잡
# https://www.acmicpc.net/problem/1764

n,m=map(int, input().split())
N=[input() for _ in range(n)]
M=[input() for _ in range(m)]
ans=sorted(list(set(N)&set(M)))

print(len(ans))
for i in ans: print(i)