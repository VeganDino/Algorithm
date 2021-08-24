# 스택
# https://www.acmicpc.net/problem/10828

import sys

n=int(sys.stdin.readline())
arr=[]

for i in range(n):
    m=sys.stdin.readline().split()
    if 'push' in m:
        arr.append(m[1])
    elif 'pop' in m:
        if arr:
            print(arr[-1])
            arr.pop()
        else: print(-1)
    elif 'size' in m:
        print(len(arr))
    elif 'empty' in m:
        if arr: print(0)
        else: print(1)
    elif 'top' in m:
        if arr: print(arr[-1])
        else: print(-1)