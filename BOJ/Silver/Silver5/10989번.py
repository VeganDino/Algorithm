# 수 정렬하기3

import sys

n=int(input())
d=[0]*100001

for i in range(n):
    d[int(sys.stdin.readline())]+=1
for i in range(10001):
    if d[i] !=0:
        for j in range(d[i]):
            print(i)