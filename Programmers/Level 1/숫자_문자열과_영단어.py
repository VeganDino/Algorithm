##### 방법 1

from collections import deque
def solution(s):
    s=deque(s)
    ans=[]
    while len(s)>0:
        if s[0].isdigit():
            ans.append(s.popleft())
        else:
                if s[0]=="z":
                    ans.append('0')
                    for _ in range(4): s.popleft()
                elif s[0]=='o':
                    ans.append('1')
                    for _ in range(3): s.popleft()
                elif s[0]=='t':
                    if s[1]=='w':
                        ans.append('2')
                        for _ in range(3): s.popleft()
                    else:
                        ans.append('3')
                        for _ in range(5): s.popleft()
                elif s[0]=='f':
                    if s[1]=='o':
                        ans.append('4')
                        for _ in range(4): s.popleft()
                    else:
                        ans.append('5')
                        for _ in range(4): s.popleft()
                elif s[0]=='s':
                    if s[1]=='i':
                        ans.append('6')
                        for _ in range(3): s.popleft()
                    else: 
                        ans.append('7')
                        for _ in range(5): s.popleft()
                elif s[0]=="e":
                    ans.append('8')
                    for _ in range(5): s.popleft()
                else: 
                    ans.append('9')
                    for _ in range(4): s.popleft()
    return int("".join(ans))


#----------------------------------------------------------

##### 방법 2

num={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', \
     'five':'5', 'six':'6', 'seven':'7','eight':'8','nine':'9'}

def solution(s):
    for key, value in num.items():
        s=s.replace(key,value)
    return int(s)