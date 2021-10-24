## 병합 정렬 (Merge Sort)

정확히 반으로 나누고 나중에 정렬             

<br>

### 순서    

1. 분할 (가장 작은 단위까지 분할)
2. 정렬 (가장 작은 단위부터 정렬)

<br>

### 시간복잡도
        
|   평균   |   최선   |   최악   |
| :------: | :------: | :------: |
| Θ(nlogn) | Ω(nlogn) | O(nlogn) |

<br>

평균, 최선, 최악 모두 항상 nlogn의 성능을 냄.  
퀵 정렬과 동일간 시간 복잡도 

<br>

```md
## 퀵 정렬 & 병합 정렬 차이점
퀵 정렬 : 우선 피벗을 통해 정렬(partition) -> 영역을 쪼갬(quickSort)
병합 정렬 : 영역을 최대한으로 쪼갬(mergeSort) -> 정렬(merge)
```  

<br>

Python의 리스트 slice notation (arr[start:end])을 사용하면 다음과 같은 코드를 작성할 수 있다.   
하지만 리스트 slice를 할 때 배열의 복제가 일어나므로 메모리 사용 효율은 좋지 않다. 

```py
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
``` 

<br>

## 최적화

병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하면 메모리 사용량을 대폭 줄일 수 있다. (In-place sort)

```py
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
```