# 소수 찾기
# https://www.acmicpc.net/problem/1978

t=int(input())
arr=list(map(int, input().split()))
count=0

for i in arr:
    cnt=0
    if i==1:
        continue
    for j in range(2, i+1):
        if i%j==0:
            cnt+=1
    if cnt==1:
        count+=1
print(count)
