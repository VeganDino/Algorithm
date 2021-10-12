###### 방법 1

def solution(sizes):
    a,b=[],[]
    for i in range(0,len(sizes)):
        if sizes[i][0]>sizes[i][1]:
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
            a.append(sizes[i][0])
            b.append(sizes[i][1])
        else:
            a.append(sizes[i][0])
            b.append(sizes[i][1])
            
    return max(a)*max(b)



###### 방법 2

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)