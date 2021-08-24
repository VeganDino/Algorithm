# 프린터 큐
# https://www.acmicpc.net/problem/1966

test=int(input())

for i in range(test):
    n,m=map(int, input().split())
    arr=list(map(int, input().split()))
    order=[0 for i in range(n)]
    order[m]=1
    cnt=0

    while True:
        if arr[0]==max(arr):
            cnt+=1
            if order[0]==1:
                print(cnt)
                break
            else:
                del arr[0]
                del order[0]
        else:
            arr.append(arr[0])
            del arr[0]
            order.append(order[0])
            del order[0]
