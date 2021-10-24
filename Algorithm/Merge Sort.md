## 병합 정렬 (Merge Sort)        

<br>

1. 분할 (가장 작은 단위까지 분할)
2. 정렬 (가장 작은 단위부터 정렬)

병합 정렬은 분할 정복 (Devide and Conquer) 기법과 재귀 알고리즘을 이용한 정렬 알고리즘이다.     
즉, 주어진 배열을 원소가 하나 밖에 남지 않을 때까지 계속 둘로 쪼갠 후에 다시 크기 순으로 재배열 하면서 원래 크기의 배열로 합친다. 

<br>

## 복잡도 분석

- 알고리즘을 큰 그림에서 보면 ```분할(split)``` 단계와 ```병합(merge)``` 단계로 나눌 수 있으며, 단순히 중간 인덱스를 찾아야 하는 분할 비용보다 모든 값들을 비교해야하는 병합 비용이 크다.
- 8 -> 4 -> 2 -> 1 식으로 전반적인 반복의 수는 점점 절반으로 줄어들 기 때문에 ```O(logN)``` 시간이 필요하며, 각 순서에서 병합할 때 모든 값들을 비교해야 하므로 ```O(N)``` 시간이 소모된다. 따라서 총 시간 복잡도는 ```O(NlogN)``` 입니다.
(평균, 최선, 최악의 시간 복잡도 모두 ```O(NlogN)```)
- 두 개의 배열을 병합할 때 병합 결과를 담아 놓을 배열이 추가로 필요하다. 따라서 공간 복잡도는 ```O(N)``` 이다.
- 다른 정렬 알고리즘과 달리 인접한 값들 간에 상호 자리 교대(swap)가 일어나지 않는다.

<br>

## 구현 

재귀를 이용해서 병합 정렬을 구현할 수 있다.     
먼저 배열을 더 이상 나눌 수 없을 때 까지 (원소가 하나만 남을 때까지) 최대한 분할 후에, 다시 병합하면서 점점 큰 배열을 만들어 나가면 된다.       
따라서 이 재귀 알고리즘의 기저 조건은 입력 배열의 크기가 2보다 작을 때이며, 이 조건에 해당할 때는 배열을 그대로 반환하면 된다.        

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

<br>

## 퀵 정렬 & 병합 정렬 차이점

```md
퀵 정렬 : 우선 피벗을 통해 정렬(partition) -> 영역을 쪼갬(quickSort)
병합 정렬 : 영역을 최대한으로 쪼갬(mergeSort) -> 정렬(merge)
```  
