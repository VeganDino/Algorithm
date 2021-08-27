from itertools import combinations

def solution(n):
    add=[]
    count=0
    combi=list(combinations(n,3))
    for i in range(len(combi)):
            add.append(sum(combi[i]))

    for n in add:
        cnt=0
        if add==1:
            continue
        for m in range(2,n+1):
            if n%m==0:
                cnt+=1
        if cnt==1:
            count+=1
    return count