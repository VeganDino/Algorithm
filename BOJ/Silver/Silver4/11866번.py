# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

from collections import deque

n,k=map(int, input().split())
Y=deque([i+1 for i in range(n)])

print("<",end='')
while Y:
    for i in range(k-1):
        Y.append(Y[0])
        Y.popleft()
    print(Y.popleft(), end='')
    
    if Y: print(", ", end='')
print(">")
