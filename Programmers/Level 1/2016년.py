##### 방법 1

def solution(a, b):
    week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    day=[31,29,31,30,31,30,31,31,30,31,30,31]
    count=b
    for i in range(a-1):
        count+=day[i]
    return week[count%7-1]


#----------------------------------------------------


##### 방법 2

def solution(a, b):
    week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    day=[31,29,31,30,31,30,31,31,30,31,30,31]
    return week[ (sum(day[:a-1]) + b-1)%7]


#----------------------------------------------------


##### 방법 3

from datetime import datetime

def solution(a,b):
    week='MON TUE WED THU FRI SAT SUN'.split()
    return week[datetime(2016,a,b).weekday()]
