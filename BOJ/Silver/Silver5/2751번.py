# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751


##### 방법 1
##### python3 : 시간초과
##### pypy3 : 맞았습니다! 1936ms

n=sorted([int(input()) for i in range(int(input()))])
for i in n: print(i)

#-----------------------------------------------------------------

##### 방법 2
##### python3 : 시간초과
##### pypy3 : 맞았습니다! 2764ms

A=[int(input()) for i in range(int(input()))]

def merge_sort(num):
    if len(num)<=1:
        return num
    
    mid=len(num)//2
    left=merge_sort(num[:mid])
    right=merge_sort(num[mid:])
    n,m,k=0,0,0
    lst=[]
    
    while n<len(left) and m<len(right):
        if left[n]<right[m]:
            lst.append(left[n])
            n+=1
        else:
            lst.append(right[m])
            m+=1
            
    lst+=left[n:]
    lst+=right[m:]
    return lst

for i in merge_sort(A):
    print(i)