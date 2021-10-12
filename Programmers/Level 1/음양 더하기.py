def solution(absolutes, signs):
    ans=0
    for a,s in zip(absolutes,signs):
        if s==True:
            ans+=a
        elif s==False:
            ans-=a
    return ans