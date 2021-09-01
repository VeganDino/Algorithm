##### 방법 1

def solution(lottos, win_nums):
    correct=6-len(set(win_nums)-set(lottos))
    cnt=lottos.count(0)
    level={6:'1', 5:'2', 4:'3', 3:'4', 2:'5', 1:'6', 0:'6'}
    for key, val in level.items():
        if key==correct: a=val
        if key==(correct+cnt): b=val
    return int(b), int(a)


#-----------------------------------------------------------


##### 방법 2

def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt=lottos.count(0)
    ans=0
    for i in win_nums:
        if i in lottos:
            ans+=1
    return rank[cnt+ans], rank[ans]