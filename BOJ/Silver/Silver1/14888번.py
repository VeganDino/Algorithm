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
