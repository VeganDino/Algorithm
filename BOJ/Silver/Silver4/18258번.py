# 큐 2
# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

n=int(sys.stdin.readline())
arr=deque()

for i in range(n):
    ans=sys.stdin.readline().split()

    if ans[0]=='push':
        arr.append(ans[1])
    elif ans[0]=='pop':
        if arr: print(arr.popleft())
        else: print(-1)
    elif ans[0]=='size':
        print(len(arr))
    elif ans[0]=='empty':
        if arr: print(0)
        else: print(1)
    elif ans[0]=='front':
        if arr: print(arr[0])
        else: print(-1)
    elif ans[0]=='back':
        if arr: print(arr[-1])
        else: print(-1)