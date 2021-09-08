# 분해합

n=int(input())

for i in range(1,n+1):
    arr=list(map(int, str(i)))
    if i+sum(arr)==n:
        print(i)
        break
    if i==n:
        print(0)