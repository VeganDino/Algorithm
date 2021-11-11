## collections 

collections 모듈은 파이썬 내장 모듈이다.    
collections 모듈은 deque,  Counter 등을 제공한다. 

<br>

## Counter

```Counter``` 모듈은 시퀀스 자료형의 데이터 요소 개수를 딕셔너리 형태로 반환하는 자료구조이다. 즉, 리스트나 문자열과 같은 시퀀스 자료형 안의 요소 중 값이 같은 것이 몇 개 있는지 반환해 준다. 

<br>

```py
from collections import Counter

text="lalalands"
Counter(text)
▶ Counter({'l': 3, 'a': 3, 'n': 1, 'd': 1, 's': 1})

t=Counter(text)
t['l']
▶ 3
```

<br>

## deque

```deque``` 모듈은 스택과 큐를 모두 지원한다. 이 모듈을 사용하기 위해서 리스트와 비슷한 형식으로 데이터를 저장해야 한다. 먼저 ```append()``` 함수를 사용하면 기존 리스트처럼 데이터가 인덱스 번호를 늘리면서 쌓이기 시작한다(스택).     
반대로 ```appendleft()``` 함수로 새로운 값을 왼쪽부터 입력하여 먼저 들어간 값부터 출력할 수 있다(큐). 

<br>

```py
from collections import deque

q=deque()
for i in range(5):
    q.append(i)
print(q)
▶ deque([0,1,2,3,4])

w=deque()
for i in range(5):
    w.appendleft(i)
print(w)
▶ deque([4,3,2,1,0])
```

<br>

```pop()``` 함수를 사용하면 오른쪽 요소부터 하나씩 추출된다.     
즉, 스택처럼 나중에 넣은 값부터 하나씩 추출할 수 있다.    
```popleft()``` 함수를 사용하면 왼쪽 요소부터 하나씩 추출된다.     
즉, 큐처럼 처음 넣은 값부터 하나씩 추출할 수 있다.     

<br>

```py
q.pop()           
▶ 4
q.pop()
▶ 3
q.popleft()
▶ 0
q
▶ deque([1,2])
```
