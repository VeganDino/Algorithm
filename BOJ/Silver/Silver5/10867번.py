# 중복 빼고 정렬하기
# https://www.acmicpc.net/problem/10867

n=int(input())
m=list(map(int,input().split()))
for i in sorted(set(m)):
    print(i, end=' ')