##### 방법 1

def solution(price, money, count):
    add=0
    for i in range(count+1): add+=i
    if (price*add) >= money:
        return (price*add)-money
    else: return 0


#------------------------------------------------

##### 방법 2

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
    