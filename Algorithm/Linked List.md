# Linked List (연결 리스트)


## Linked List

- Linked list는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조 or 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료구조
- Python의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있다.
- Array list와 다르게 엘리먼트와 엘리먼트 간의 연결(link)을 이용해서 리스트를 구현한 것
- Array list에서는 엘리먼트라는 이름을 사용했지만 linked list와 같이 연결된 엘리먼트들은 ```노드(node, 마디, 교점)``` 혹은 ```버텍스(vertex, 정점, 꼭지점)```라고 부르먀, 각 노드 안에서, 다음이나 이전의 노드와 연결 정보를 가지고 있는 공간을 ```포인터(pointer)```라고 한다. 

<br>

<img src = "https://user-images.githubusercontent.com/56749776/134843275-7b5f4070-fa6f-4ff3-bed1-8d7aabb19238.png" width="80%">

<br>
<br>

## Node 구현

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

<br>

## Linked list 구현

```py
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)   

    # header부터 탐색해 뒤에 새로운 노드 추가하기
    def append(delf, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
```

<br>

## Node index 알아내기

```py
def get_node(self, index):
    cnt = 0
    node = self.head
    while cnt < index:
        cnt += 1
        node = node.next
    return node
```

## 삽입

```py
def add_node(self, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    node = self.get_node(index-1)
    next_node = node.next
    node.next = new_node
    new_node.next = next_node
```

<br>

## 삭제

```py
def delete_node(self, index):
    if index == 0:
        self.head = self.head.next
        return
    node = self.get_node(index-1)
    node.next = node.next.next
```

<br>

## 전체 코드

```py
# Node 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList 클래스 (자료구조) 정의
class LinkedList:

    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before # 중요 : current가 next가 아닌 before로 변경된다.
        #

        self.num_of_data -= 1

        return pop_data

    # first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0: # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data
```