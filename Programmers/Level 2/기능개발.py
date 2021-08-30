##### 방법 1

def solution(progresses, speeds):
    minus=[]
    # minus는 100에서 progresses 각 원소를 뺀 수
    for i in range(len(speeds)):
        minus.append(100-progresses[i])
    count=[]
    # count는 minus에서 100에 도달하기 위해 몇일 걸리는지
    for i in range(len(speeds)):
        if minus[i]%speeds[i]==0:
            count.append(minus[i]//speeds[i])
        else:
            count.append(minus[i]//speeds[i]+1)
    cnt=1
    ans=[]
    # ans 배포마다 몇 개의 기능이 배포되는지
    start=count[0]
    for i in range(len(count)-1):
        if start>=count[i+1]:
            cnt+=1
        else:
            ans.append(cnt)
            cnt=1
            start=count[i+1]
    if start>=count[-1]:
        ans.append(cnt)
    else: ans.append(cnt)
        
    return ans


#-------------------------------------------


##### 방법 2

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


    '''
    Example

    ▶ Input
    solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])

    ▶ Output
    [[5, 1]]
    [[5, 1], [10, 1]]
    [[5, 1], [10, 2]]
    [[5, 1], [10, 3]]
    [[5, 1], [10, 3], [20, 1]]
    [[5, 1], [10, 3], [20, 2]]

    [1, 3, 2]
    '''