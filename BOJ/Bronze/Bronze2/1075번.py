# 나누기
# https://www.acmicpc.net/problem/1075

n,f=input(),int(input())

for i in range(100):
    if len(str(i))==1:
        if int(n[:-2]+str(f'0{i}'))%f==0:
            print(f'0{i}')
            break
    else: 
        if int(n[:-2]+str(i))%f==0:
            print(i)
            break