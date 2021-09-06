# 단어 뒤집기
#  https://www.acmicpc.net/problem/9093

n=int(input())
for _ in range(n):
    m=input().split()
    arr=[]
    
    for i in m:
        reverse=i[::-1]
        arr.append(reverse)
    print(' '.join(arr))