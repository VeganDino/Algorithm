## Bubble Sort

※ 오름차순을 기준으로 정혛

인접한 두 원소를 검사하여 정렬하는 알고리즘.    
인접한 2개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환한다.      
선택 정렬과 기본 개념 유사하다. 

<br>

<img src='https://user-images.githubusercontent.com/56749776/138304266-9efe4271-6c1f-4fbe-ab67-565244027ee2.png' width='100%'>

<br>

```py
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for num in reversed(range(len(x))):
        for i in range(num):
            if x[i] > x[i+1]:
                swap(x, i, i+1)
```