def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt=0
        for j in range(i, len(prices)-1):
            if prices[i]<=prices[j]:
                cnt+=1
            else: break
        answer.append(cnt)
    return answer 
