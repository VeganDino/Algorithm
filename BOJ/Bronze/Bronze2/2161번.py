# 카드1
# https://www.acmicpc.net/problem/2161

from collections import deque

n=int(input())
m=deque([i+1 for i in range(n)])
card=[]

while len(m) > 1:
    card.append(m.popleft())
    m.append(m.popleft())

card.append(m[0])
for i in card: print(i, end=' ')




''' 긴버전
from collections import deque

n=int(input())
m=deque([i+1 for i in range(n)])
card=[]

while len(m) > 1:
    left = m.popleft()
    card.append(left)

    left = m.popleft()
    m.append(left)

card.append(m[0])
for i in card:
    print(i, end=' ')
'''
