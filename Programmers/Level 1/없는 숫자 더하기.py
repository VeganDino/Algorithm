def solution(numbers):
    n=[0,1,2,3,4,5,6,7,8,9]
    answer = set(n)-set(numbers)
    return sum(answer)