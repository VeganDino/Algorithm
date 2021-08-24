# GCD 합
# https://www.acmicpc.net/problem/9613

from math import gcd
from itertools import combinations

t=int(input())
for i in range(t):
    cnt=0
    n=list(map(int, input().split()))
    arr=list(combinations(n[1:],2))
    
    for j in arr:
        cnt+=gcd(j[0], j[1])
    print(cnt)
    