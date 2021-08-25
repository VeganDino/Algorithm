# 카드2
# https://www.acmicpc.net/problem/2164


##### 방법 1
##### python3 248ms

from collections import deque

n=int(input())
m=deque([i+1 for i in range(n)])

while len(m)>1:
    m.popleft()
    m.append(m.popleft())
print(m[0])


#-----------------------------------------------------


##### 방법 2
##### python3 72ms

n=int(input())
m=n
cnt=0

while n>1:
    n=n//2
    cnt+=1

if m==2**cnt:
    print(m)
else:
    print((m-2**cnt)*2)

'''
(입력값,마지막으로 남는 카드숫자) 
(1,1) 
(2,2) (3,2) 
(4,4) (5,2) (6,4) (7,6) 
(8,8) (9,2) (10,4) (11,6) (12,8) (13,10) (14,12) (15,14) 
(16,16) (17,2) ⋯

마지막으로 남는 카드숫자만 보면
1
2 2
4 2 4 6
8 2 4 6 8 10 12 14 
16 2 4 6 8 10 12 14 16 18 ⋯ 30
32 2 4 ⋯ 62
⋯

각 줄의 첫번째 수는 2**(a) 값이다.
따라서 입력값 n이 2로 몇번 나누어지는지 확인한 뒤(=cnt),
2**cnt과 2**(cnt+1) 사이 값들은 모두 2의 배수 (2×1, 2×2, 2×3, 2×4 ⋯)이므로
2×(n-2**cnt)을 출력하면 된다.
 
'''
