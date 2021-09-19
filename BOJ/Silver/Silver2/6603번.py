# 로또


###### 방법 1-1 68ms

from itertools import combinations

while True:
    n=list(map(int,input().split()))
    if n==[0]:
        break
    a=list(combinations(n[1:],6))
    for j in a:
        print(j[0],j[1],j[2],j[3],j[4],j[5])
    print()

#----------------------------------------------------


###### 방법 1-2 72ms

from itertools import combinations

lst=[]
while True:
    n=list(map(int,input().split()))
    lst.append(n)
    if n==[0]:
        break
        
for i in range(len(lst)-1):
    a=list(combinations(lst[i][1:],6))
    for j in a:
        print(j[0],j[1],j[2],j[3],j[4],j[5])
    print()

#----------------------------------------------------


###### 방법 2 76ms

import sys
from itertools import combinations

while True:
    input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if input_list[0] == 0:
        break

    for i in combinations(input_list[1:], 6):
        print(str(i).replace("(", "").replace(")", "").replace(",", ""))
    print()