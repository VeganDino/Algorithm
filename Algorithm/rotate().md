# 파이썬 리스트 목록 회전시키기

```py
def rotate(a,n):
    return a[n:]+a[:n]

a=[1,2,3,4]
rotate(a,1)            # [2,3,4,1] 반시계 방향으로
```

<br>

# Collections.depue() 에서 rotate() 함수
```py
from collections import deque
items=deque([1,2])
items.append(3)         # items=[1,2,3]
items.rotate(1)         # tiems=[3,1,2] 시계 방향으로
items.rotate(-1)        # 초기 item으로 변환 items=[1,2,3]
```
