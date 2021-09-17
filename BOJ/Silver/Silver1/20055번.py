# 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int, input().split())   # 벨트 길이 n, 내구도 0인 칸 k
belt=deque(list(map(int, input().split())))  # 위치마다 내구도
robot=deque([0]*n)
level=0

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1]=0 # 로봇이 내려가는 부분으로 0
    
    if sum(robot): # 로봇이 존재하면
        for i in range(n-2,-1,-1): # n-1는 로봇이 내려가는 부분이므로 n-2부터
            if robot[i]==1 and robot[i+1]==0 and belt[i+1]>=1:
                robot[i+1]=1
                robot[i]=0
                belt[i+1]-=1
        robot[-1]=0 
    
    if robot[0]==0 and belt[0]>=1:
        robot[0]=1
        belt[0]-=1
    level+=1
    
    if belt.count(0) >=k:
        print(level)
        break