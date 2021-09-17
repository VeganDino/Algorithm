# rotate()

### 파이썬 리스트 목록 회전시키기

```py
def rotate(a,n):
    return a[n:]+a[:n]

a=[1,2,3,4]
rotate(a,1)            # [2,3,4,1] 반시계 방향으로
```

<br>

### Collections.depue() 에서 rotate() 함수
```py
from collections import deque
items=deque([1,2])
items.append(3)         # items=[1,2,3]
items.rotate(1)         # tiems=[3,1,2] 시계 방향으로
items.rotate(-1)        # 초기 item으로 변환 items=[1,2,3]
```

<br>

# roll()

### numpy 에서 roll() 함수

```py
n=numpy.arange(1,10)
#▶ array([1, 2, 3, 4, 5, 6, 7, 8, 9])

numpy.roll(n,1)
#▶ array([9, 1, 2, 3, 4, 5, 6, 7, 8])

numpy.roll(a,-1)
#▶ array([2, 3, 4, 5, 6, 7, 8, 9, 1])

numpy.roll(a,5)
#▶ array([5, 6, 7, 8, 9, 1, 2, 3, 4])

numpy.roll(a,9)
#▶ array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```