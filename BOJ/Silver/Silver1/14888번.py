# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888


###### 방법 1 순열 
###### pypy3 980ms , python3 시간초과


from itertools import permutations
import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
op_num=list(map(int, input().split())) # + - x ÷
oper=['+','-','*','/']
lst=[]
mini=1e9                               # =1*10^9 = 1000000000
maxi=-1e9

for i in range(4):
    for j in range(op_num[i]):
        lst.append(oper[i])

def calculate():
    global mini, maxi
    for i in permutations(lst,n-1):
        math=a[0]
        for j in range(1,n):
            if i[j-1]=='+':
                math+=a[j]
            elif i[j-1]=='-':
                math-=a[j]
            elif i[j-1]=='*':
                math*=a[j]
            elif i[j-1]=='/':
                math=int(math/a[j])
        if math>maxi:
            maxi=math
        if math<mini:
            mini=math
            
calculate()
print(maxi)
print(mini)



#----------------------------------------------------------


###### 방법 2 DFS
###### pypy3 212ms , python3 100ms


import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
op=list(map(int, input().split()))
mini=1e9
maxi=-1e9

def dfs(d, math, plus, minus, multi, divide):
    global mini, maxi
    if d==n:
        maxi=max(math, maxi)
        mini=min(math, mini)
        return
    
    if plus:
        dfs(d+1,math+a[d],plus-1, minus, multi, divide)
    if minus:
        dfs(d+1,math-a[d],plus, minus-1, multi, divide)
    if multi:
        dfs(d+1,math*a[d],plus, minus, multi-1, divide)
    if divide:
        dfs(d+1,int(math/a[d]),plus, minus, multi, divide-1)

dfs(1,a[0],op[0],op[1],op[2],op[3])
print(maxi)
print(mini)