# 스택 수열
# https://www.acmicpc.net/problem/1874

'''
n=int(input())
seq=[int(input()) for i in range(n)]
num=[i+2 for i in range(n-1)]
arr=[1]

while arr:
    if arr[-1] != seq[0]:
        arr.append(num[0])
        print('+')
        del num[0]
    else: 
        print('-')
        arr.pop()
'''

import math
print(math.lcm(10,12))