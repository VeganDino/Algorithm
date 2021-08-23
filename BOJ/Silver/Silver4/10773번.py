# 제로
# https://www.acmicpc.net/problem/10773

''' 방법 1 '''
##### python3 : 시간초과
##### pypy3 : 맞았습니다!

k=int(input())
lis=[int(input()) for _ in range(k)]
cnt=[]

for i in lis:
    if i==0:
        cnt.pop()
        # cnt[:-1]로 할 경우 pypy3시간 : 2412ms
        # cnt.pop()로 할 경우 pypy3시간 : 292ms
    else:
        cnt.append(i)

print(sum(cnt))
    

