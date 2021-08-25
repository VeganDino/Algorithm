# 최대공약수와 최소공배수 
# https://www.acmicpc.net/problem/2609

'''
최대공약수 GCD(Greatest Common Divisor)
최소공배수 LCM(Largest Common Multipul)

[유클리드 호제법]
x,y의 최대공약수 = y,r의 최대공약수  (x%y=r)
'''

##### 방법 1

n,m=map(int, input().split())

def gcd(n,m):
    while m:
        n,m=m,n%m
    return n

def lcm(n,m):
    return (n*m)//gcd(n,m)

print(gcd(n,m))
print(lcm(n,m))

#-----------------------------------------------

##### 방법 2

import math 

n,m=map(int, input().split())
print(math.gcd(n,m))
print((n*m)//math.gcd(n,m))
