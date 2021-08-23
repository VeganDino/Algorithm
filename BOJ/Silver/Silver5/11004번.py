# K번째 수
# https://www.acmicpc.net/problem/11004

n,k=map(int, input().split())
a=sorted(list(map(int, input().split())))
print(a[k-1])


