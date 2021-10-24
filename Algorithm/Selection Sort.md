## 선택 정렬 (Selection Sort)

<br>

정렬 알고리즘 중에서 가장 직관적이고 쉽게 구현 가능한 정렬이다. 

<br>

|Index|Value|
|------|------|
|0|모든 값 중 가장 작은 값|
|1|첫번째 값(Index=0)을 제외하고 남은 값 중에서 가장 작은 값|
|⋯|⋯|
|i|i번째부터 n-1번째까지 값 중 가장 작은 값|
|⋯|⋯|
|n-2|n-2번째와 n-1번째까지 값 중 가장 작은 값|
|n-1|마지막에 남은 하나의 값 (비교 대상 없음)|

<br>

크기 n의 배열이 주어졌을 때, index 0부터 n-1까지의 모든 index i에 대해서, i번째 부터 n-1 번째까지 값 중 가장 작은 값을 구해서 index i에 놓으면 정렬된 배열을 얻을 수가 있다. 모든 index에 대해서 그 index에 위치시킬 값을 “선택”하기 때문에 이 정렬 알고리즘을 **선택 정렬**또는 **Selection Sort**이라고 부른다.

<br>

## 복잡도 분석

- 선택 정렬은 별도의 추가 공간을 사용하지 않고 주어진 배열이 차지하고 있는 공간 내에서 값들의 위치만 바꾸기 때문에 ```O(1)```의 공간 복잡도를 가진다.
- 시간 복잡도는 우선 루프문을 통해 모든 인덱스에 접근해야 하기 때문에 기본적으로 ```O(N)```을 시간을 소모하며, 하나의 루프에서는 현재 인덱스의 값과 다른 인덱스의 값들과 비교하여 최소값을 찾은 후 현재 인덱스에 있는 값과 상호 자리 교대를(swap)해야 해야하기 때문에 ```O(N)```을 시간이 필요하게 된다. 따라서 선택 정렬은 총 ```O(N²)```의 시간 복잡도를 가지는 정렬 알고리즘이다.

<br>

## 알고리즘 특징

- 선택 정렬은 정렬된 값을 배열의 맨 앞부터 하나씩 채워나가게 된다. 따라서, 뒤에 있는 index로 갈수록 비교 범위가 하나씩 점점 줄어드는 특성을 가지고 있다. (index 0에서는 0부터 n-1까지 비교해야 되지만, index n-1에서는 남은 숫자가 하나 밖어서 비교가 필요 없음)
- 입력 배열이 이미 정렬되어 있건 말건 관계없이 동일한 연산량을 가지고 있기 때문에 최적화 여지가 적어서 다른 ```O(N²)``` 대비해도 성능이 떨어지는 편이다.
- 이러한 성능 상의 한계 때문에 실전에서는 거의 보기 힘들지만 가장 구현이 쉬운 정렬 알고리즘이라서 알고리즘 수업 시간에는 한 번씩 꼭 접하게 되는 유명한 정렬 알고리즘이다.

<br>

## 구현

- 두 개의 반복문이 필요하다.      
- 내부 반복문에서는 현재 index부터 마지막 index까지 최소값의 index를 찾아내고, 외부 반복문에서는 이 최소값의 index와 현재 index에 있는 값을 상호 교대(swap)한다.      
- 외부 반복문에서는 index i를 0에서 n-2(또는 n-1. 마지막 index에서는 남는 값이 하나 밖에 없기 때문에 대세에 지장 없음)까지 진행시키며, 내부 반복문에서 이미 정렬된 값들에서는 관심이 없기 때문에 index j를 i에서 n-1까지 진행시킨다.      
- 각 index에 대해서 최소값을 찾기 위해 대소 비교는 여러번 일어나나 상호 교대(swap)은 딱 한번만 알어난다.

<br>

<img src ='https://user-images.githubusercontent.com/56749776/138605807-2d3dad52-44ff-44ef-b686-44c3ff9ac626.png' width='40%'>


```py
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```