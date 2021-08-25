# 요세푸스 문제
# https://www.acmicpc.net/problem/1158

n,k=map(int, input().split())
Y=[i+1 for i in range(n)]
cnt=k-1 # 원을 도는 주기, 위치
lst=[]

for i in range(n):
    if len(Y)>cnt:             
        lst.append(Y.pop(cnt))    # 원 주기대로 해당되는 인덱스의 값 제거
        cnt+=k-1
    else:
        cnt%=len(Y)  # 위치가 len(Y) 넘는 경우(한바퀴 다 돌았을 경우)
                     # 리스트 Y 길이를 주기로 나눈 나머지를 인덱스로 하는 값 제거   
                     # 3명 중 5번 째 사람 구할 때 5%3=2, 즉 2번 째 사람 = 5번 째 사람                         
        lst.append(Y.pop(cnt))
        cnt+=k-1
print(f"<{', '.join(str(i) for i in lst)}>")
