## Chap 1. 자료구조를 배우기 위한 준비

### 자료구조 
: 현실세계의 데이터들을 논리적으로 나열하여 표현하고 컴퓨터가 (시간, 공간) 효율적으로 처리할 수 있도록 컴퓨터 메모리에 저장하는 방법
- 특정 문제 해결에 대한 ADT의 연산이 가장 효율적으로 수행될 수 있도록 데이터들에 대한 논리적 구조를 설계하고 저장한 것
- 예시 
  - 선형탐색( linear search ) 알고리즘 : 무작위로 있는 데이터에서 사용 O(N)
  - 이진탐색( binary search ) 알고리즘 : 나열된 데이터에서 사용 O(logN)- 데이터가 자주 삽입/삭제 된다면 선형탐색 알고리즘에 비해 시간적으로 효율적이진 않음
  - 이진탐색트리( BST : Binary Search Tree ) : 균형 잡힌 트리라면, 검색/삽입/삭제 연산도 빠르게 할 수 있음 O(logN) 하지만, 편향된 BST 형태라면 ②비해 시간적으로 효율적이진 않음


### Data Abstraction 
: 현실 세계의 특정 유/무형 개체를 데이터로 표현하기 위해 해당 개체의 공통적이고 핵심적인 특징만을 간추려 내는 것. 
- 즉, 데이터들의 논리적 구조 및 관련 연산을 구체적으로 어떻게 프로그램으로 구현해야 한다는 세부 사항을 숨기는 것


### ADT ( Abstract Data Type)
: 사용자의 입장에서 문제해결의 대상이 되는 데이터들의 집합 D와 D에 대한 연산들을 묶어서 정의해 놓은 것
- 사용하는 이유 : 사용자의 입장에서는 구체적으로 데이터들이 어떻게 논리적으로 나열되고 물리적으로 저장되는지, 어떻게 연산이 수행되는지 알고 싶지 않기 때문 


## Chap 2. Linked List
: 리스트의 항목들을 메모리에 분산하여 저장하고(= 메모리에 연속적으로 저장할 필요 없음) 각 항목은 다음 순서의 항목이 저장된 위치를 가리키는 link를 가짐으로써 순서 유지

```python
class Node:
  def __init__(self, item):
    self.item = item #data field
    self.next = None #link field
```

### Singly Linked List
: 각 item을 저장하고 있는(data field) 노드의 link field를 참조가 다음 순서의 노드를 가리키도록 만들어 모든 노드들을 한 줄로 연결시킨 자료구조
- 마지막 노드의 참조는 None


### Ordered Linked List
: 정렬된 노드 순서로 연결된 단순 연결 리스트


### Circular Linked List
+ 마지막 노드가 첫 노드와 연결된 단순 연결 리스트
+ 황형이므로 연결 리스트의 어떤 노드도 첫 노드가 될 수 있음
+ head가 마지막 노드를 참조하게 함으로써 첫노드와 마지막 노드를 o(1) 시간에 접근할 수 있도록 함

|                         | Singly Linked List | Circular Linked List | List |
|-------------------------|--------------------|----------------------|------|
| Search via index        | o(n)               | o(n)                 | o(1) |
| Search via item         | o(n)               | o(n)                 | o(n) |
| Insert at first index   | o(1)               | o(1)                 | o(n) |
| Insert into which index | o(n)               | o(n)                 | o(n) |
| Insert at last index    | o(n)               | o(1)                 | o(1) |
| Delete first item       | o(1)               | o(1)                 | o(n) |
| Delete via item         | o(n)               | o(n)                 | o(n) |
- 단, 정렬된 list의 검색 기능은 이진 탐색(o(log n))을 사용하여 항상 Singly Linked List보다 좋음  
- Ordered Linked List에서도 검색이 o(n)이므로 시간 효율적인 탐색을 위해서 정렬할 필요가 없음 


## Chap 3. Stack & Queue

### Stack
: Top에서만 새로운 항목을 push하거나 Pop하는 논리적 선형 구조 
- LIFO : Last-In, First-out 구조
- list나 Singly Linked List로 구현했을 시, push/pop 연산의 시간복잡도는 o(1)

### Queue
: Rear에서 새로운 항목을 Enqueue하고, Front에서 기존 항목을 Dequeue하는 논리적 선형 구조
- FIFO : First-in, First-out 구조
- list로 구현할 시 enqueue : O(1), dequeue : O(n)
- singly linked list로 구현할 시 enqueue : O(n), dequeue : O(1)
- circular linked list로 구현할 시 enqueue : O(1), dequeue : O(1)  


## Chap 4. Tree

### Tree
: 비선형 구조인 트리는 다음의 재귀적인 정의를 따르는 조건을 만족하는 **하나** 이상의 노드들로 구성된 유한 집합 T로, 노드는 트리의 기본 단위로 사용됨
- 노드 중에는 Root라는 노드가 존재함
- Root를 제외한 나머지 노드들은 **원소가 중복되지 않는 N(>=0)개의 부분집합** T1, T2, ..., TN으로 나누어지며, Ti는 하나의 트림
- 이때, 각 Ti를 트리 T의 Subtree라고 부름
- 계층 구조를 효과적으로 표현함.
- 트리의 용어
  + Non-leaf Node = Internal Node : leaf node를 제외한 모든 
  + Degree( 차수 ) : 특정 노드의 자식 노드 수
  + Degree of Tree : 트리에 존재하는 모든 노드가 가지는 차수 값 중 가장 큰 값
  + Path( 경로 ) : 노드 A에서 노드 B까지 간선으로 연결된 노드들과 A, B를 포함한 리스트로 경로에 속한 노드는 중복되지 않음
  + Ancestor Node( 조상 노드 ) : 노드 A에서 노드 B까지의 경로 상에 존재하는 노드 중 노드 A를 제외한 노드들
  + Descendant Node( 후손 노드 ) : 특정 노드를 Root로 하는 트리에서 해당 노드를 제외한 노드들
  + Level / Depth : 임의의 노드로부터 Root 노드까지 경로 상에 존재하는 간선의 수
    + Root의 level은 0임  
  + Height of Tree : Level 값 중 가장 큰 값
  + Key : 노드에 저장된 정보 중 탐색 시 사용되는 정보 
 
 #### Left Child - Right Sibling 표현
 - 차수가 K인 트리 T에 존재하는 노드의 수가 N개일 때, None 값을 저장하고 있는 link field의 수 = NxK -(N-1)
   + NxK : T에 존재하는 모든 link field의 수
   + N-1 : T에서 부모 노드와 자식 노드를 연결하는 간선의 수
   
 ![image](https://user-images.githubusercontent.com/65997635/128204254-88b81300-744e-4100-94b2-ea04e078dccf.png)
 
 ![image](https://user-images.githubusercontent.com/65997635/128204366-8479881e-6692-4df4-be7b-6917e420b4a5.png)
 
 - 차수를 2로 제한하여 각 노드는 자신의 제일 왼쪽 자식과 자신의 오른쪽 남매에 대한 두 개의 참조를 저장하는 link field를 가짐
 
 
### Binary Tree
: 재귀적으로 정의되며, empty이거나 Root를 기준으로 왼쪽 서브트리와 오른쪽 서브트리로 구성된 트리
 
#### 이진 트리의 특징
+ 트리는 자식 노드의 순서를 구별하지 않지만, **이진 트리는 자식노드의 순서를 구별함**
+ 트리는 empty인 트리가 존재하지 않지만, **이진 트리는 empty인 트리가 존재함**
+ 레벨 i에 존재할 수 있는 최대 노드의 수 = 2^i
+ 이진 트리에 존재하는 노드의 수가 N일 때 해당 트리의 최대 높이 h = N-1
+ T[i] 노드의 왼쪽 자식 노드= T[2*i+1] 
+ T[i] 노드의 오른쪽 자식 노드= T[2*(i+1)] 
+ T[i] 노드의 부모 노드= T[(i-1)//2] ( i > 0 )
+ 총 노드 수 구하는 코드
```python
def Count_Nodes(self, root):
  if root.right_child :
    r = Count_Nodes(root.right_child)
  if root.left_child :
    l = Count_Nodes(root.left_child)
  return 1 + r + l
```

+ 높이 구하는 코드
```python
def Height(self, root):
  if root.right_child :
    r = Height(root.right_child)
  if root.left_child :
    l = Height(root.left_child)
  return 1 + max(r, l)
```

+ leaf node 수 = (자식이 2개인 노드의 수) + 1 
```
  n = n0 + n1 + n2 
  간선 수 n-1 = n1 + 2n2 
  연립하면 n0 = n2+1
  ( 이때, n0은 leaf node 수, n1은 하나의 자식을 갖는 node 수, n2는 두개의 자식을 갖는 node 수이다.)
```

#### 특별한 형태의 이진 트리
+ Prefect Binary Tree( 완벽 이진 트리 ) : 각 내부 노드가 두개의 자식 노드를 가지는 이진 트리
  + 모든 노드의 수 : 2^(h+1)-1 
  + 높이 h = log2(n+1) -1  
  + 특정 레벨에 있는 노드 수 = 올림(n/2^i)
    + 7개의 노드를 가진 완벽 이진 트리에서 비 단말노드들의 개수 = 올림(7/2) = 4
    + 그 전 레벨 노드들의 개수 = 올림(7/4) = 2
   
+ Complete Binary Tree ( 완전 이진 트리 ) : 마지막 레벨을 제외한 각 레벨이 모두 두개의 자식 노드를 가지며, 마지막 레벨에는 왼쪽부터 빠짐없이 채워진 트리
  + 높이가 h인 완전 이진 트리에 존재할 수 있는 노드의 수(N) = 2^h <= N <= 2^(h+1)-1  
  + 높이 h = 올림( log2(N+1) ) - 1
+ Full Binary Tree( 포화 이진 트리 ) : 자식 노드의 수가 2 또는 0으로 구성된 이진 트리

#### Traversal ( 순회 ) 
- 깊이 우선 ( Depth-First Search ) **o(n)**
  + Preorder ( 전위 순회, NLR ) 
  + Inorder ( 중위 순회, LNR )
  + Postorder ( 후위 순회, LRN )
- 너비 우선 ( Breadth-First Search ) **o(n)**
  + Levelorder ( 레벨 순회 ) : queue 사용

#### Binary Search Tree (BST)
: 이진 탐색 개념을 트리 구조에 접목한 자료구조
- 모든 노드들의 키는 서로 다른 **유일한값**을 가짐
- 특정 노드 N의 키 값이 N의 왼쪽 서브 트리에 존재하는 모든 노드의 키 값보다 크고, N의 오른쪽 서브 트리에 있는 모든 노드들의 키 값보다 작음
- 따라서, **Inorder ( 중위 순회, LNR )** 시 키 값이 정렬되어 출력됨
- Search / Insert / Delete의 시간 복잡도 : o(h) → o(log N) 만약, 편향된 이진 탐색 트리인 경우 o(N)
- Delete의 경우, 자식노드의 수에 따라 case를 3가지(자식노드 수 = 0 or 1 or 2)로 분류할 수 있음
  - 자식 노드의 수가 2개인 경우, **중위 선행자**( n의 왼쪽 트리 중 가장 큰값 ) 또는 **중위 후속자**( n의 오른쪽 서브 트리에서 가장 작은 값 )를 선택하여 트리를 이어야함  


#### Heap

##### Priority Queue
: 임의의 기준을 중심으로 가장 높은 우선순위를 가지는 항목의 삭제 및 반환과 임의의 우선순위를 가지는 항목 삽입을 지원하는 자료구조
- 예시
  - stack : 시간 중심으로 가장 마지막에 삽입된 항목이 가장 높은 우선순위를 가짐
  - queue : 시간 중심으로 가장 처음에 삽입된 항목이 가장 높은 우선순위를 가짐

##### Heap 
: 완전 이진 트리로서 힙속성(Heap Property)을 유지하는 자료 구조
- Heap Property : 부모 노드의 키 값이 우선순위가 자식 노드의 키 값의 우선순위보다 높음 
  - Max Heap : 키 값이 큰 항목이 우선순위가 높음
  - Min Heap : 키 값이 작은 항목이 우선순위가 높음
- Insert / Delete의 시간 복잡도 : o(h) → o(log N)
- Heapify : 리스트를 힙으로 만듦
  1. Top-down (하향식) 알고리즘 : list의 각 항목을 Insert하여 힙 완성 o(log N) * N = o(N log N) 
  2. Bottom-up (상향식) 알고리즘 : list의 항목을 완전 이진 트리로 간주하고, 마지막 비단말 노드를 시작으로 root 노드까지의 서브 트리에 대해 downheap()을 사용하여 힙 속성을 충족시킴
    - downheap 수행 순서 : 오른쪽 → 왼쪽, 아래 → 위
    - 시간 복잡도 : o(n)
    - leaf node( 단말 노드 ) index : n//2 ~ n-1

    ```python
    def heapify(self, array): # o(n)
        for i in range(len(array)//2-1, -1, -1):
            self.downheap(i)

    def downheap(self, i):
        while 2*i + 1 <= self.size()-1:
            k = 2*i+1
            if k < self.size()-1 and self.items[k] > self.items[k+1]:
                k += 1
            if self.items[i] < self.items[k]:
                break
            self.swap(i, k)
            i = k
    ```
|                             | Enqueue  | Dequeue  |
|-----------------------------|----------|----------|
| list                        | o(1)     | o(n)     |
| sorted list                 | o(n)     | o(1)     |
| singly linked list          | o(1)     | o(n)     |
| sorted singly linked list   | o(n)     | o(1)     |
| circular linked list        | o(1)     | o(n)     |
| sorted circular linked list | o(n)     | o(1)     |
| Heap                        | o(log n) | o(log n) |

## Chap 5. Hashing
: 데이터 키 값을 함수를 사용해 변환한 값을 리스트의 인덱스로 사용하여 데이터를 리스트에 저장하는 절차  

### 사용 동기 
: 시간 복잡도가 o(log n)보다 빠른 검색 방법은 없을까? 인덱스를 통한 검색 o(1)
- 하지만, 메모리 낭비가 심할 수 있음. 
- 따라서, 공간 낭비를 줄이면서 데이터 검색의 시간 복잡도를 o(1)로 유지하기 위해 사용
- hash function을 통해 큰 키 공간(key space/domain)을 작은 주소 공간(address space)으로 변환
  - hash function( 해쉬 함수 ) : 해싱에 사용되는 함수
  - hash value( 해쉬 값 ) or hash address(해시 주소): 해쉬 함수가 계산한 값
  - hash table( 해시 테이블 ) : 해시 데이터가 해시 값에 따라 저장된 구조 
    + m개의 버킷으로 이루어진 테이블이며, 각 버킷은 s개의 슬롯을 가질 수 있음
    + ex) list : 7개의 item을 가졌다면 이는, 7개의 버킷이 각각 1개의 슬롯을 가져서 총7개의 슬롯을 가진 형태
    + 버킷이 가지는 슬롯 수보다 많이 충돌이 발생하면 버킷에 더 이상 데이터를 저장할 수 없게 되는 오버 플로우가 발생함
    + 따라서, list는 슬롯이 1개이므로 충돌이 한번만 발생하도 오버플로우가 발생하여 충돌을 해결할 방법이 필요
  - loading factor( 적재율 ) : 저장되는 데이터 수(n)과 해시테이블의 크기(m)의 비율 = n/m
  
### 좋은 hash function의 조건
- hash value가 주소 공간 내에 균등하게 분포해야 함
- 충돌( collision ) 빈도가 잦지 않아야 함
  - 하지만, 일반적으로 큰 키 공간을 작은 주소 공간으로 변환하기 때문에 충돌이 발생할 수 밖에 없음
- 계산이 빨라야 함

### 충돌 해결 방법
1. 개방주소 방식
: 충돌이 발생하면 해시 테이블 내의 새로운 슬롯을 조사하여 충돌된 데이터를 삽입하는 방식
- 처음에 주어진 해시 테이블의 공간 안에서 충돌을 해결하므로 퍠쇄 해싱(closed hashing)
- 선형 조사, 이차조사, 랜덤 조사, 이중 해싱

2. 폐쇄주소 방식
: 충돌이 발생하더라도 키 값에 대한 해시값을 가지는 슬롯에만 데이터를 삽입하는 방식
- 처음에 주어진 해시 테이블의 공간 밖에 새로운 공간을 할당하여 충돌을 해결하므로 개방 해싱(open hasing)
- 체이싱

#### Linear Probing (선형 조사) 방법
: Insert 시 충돌이 일어난 슬롯부터 순차적으로 방문하여 처음 발견한 empty 슬롯에 데이터를 삽입하는 방식
- 문제점 
  - clustering 현상 발생 
    - 충돌 시 순차적으로 빈 슬롯을 찾아 데이터를 저장하므로 해시 테이블 내의 데이터들이 빈틈없이 뭉쳐지는 현상
  - clustering 현상은 Insert / Search / Delete 시 군집된 데이터를 순차적으로 확인해야하므로 선형 검색과 유사하게 됨

#### quadratic probing (이차 조사) 방법
: Insert 시 충돌이 일어난 슬롯부터 (key+1)%m, (key+4)%m, (key+9)%m ,,, 순서로 방문하여 처음 발견한 empty 슬롯에 데이터를 삽입하는 방식
- 선형 조사의 군집화 현상의 문제점을 해결할 수 있음
- 해시 테이블의 크기 m이 소수(prime number)이고 적재율 < 0.5인 경우, 반드시 empty 슬롯을 찾을 수 있음
- 문제점
  - 서로 다른 키 값을 가지는 데이터가 같은 해시 값을 가지게 되는 경우, 똑같은 점프 순서로 탐색하므로 또 다른 형태의 2차 군집화 현상이 발생함
  - empty 슬롯이 존재하는데도 empty 슬롯을 건너뛰어 삽입에 실패하는 경우 생김
    - 즉, 해시 테이블이 꽉 찬 상태가 아니어도 empty 슬롯을 반드시 발견한다고 보장할 수 없음
  - 적재율 > 0.5인 경우, 삽입 검색 삭제를 위한 슬롯 방문수가 급격하게 증가함

#### Chaining (체이닝) 방법
: 해시 테이블의 각 소켓이 한 개 이상의 데이터를 저장할 수 있도록 충돌된 데이터들의 단순 연결 리스트를 저장
- 해시 테이블의 각 항목 table[i]는 해시 값 i를 가지는 데이터들을 저장하는 노드들의 연결리스트의 첫 노드를 가리키는 head 역할을 함
- 해시 테이블의 적재율(loading factor)인 알파에 큰 영향을 받지 않음
- 나눗셈 해시 함수와 체이닝을 사용할 경우 가장 좋은 성능을 보임

## Chap 6. Sort

### Selection Sort ( 선택 정렬 )
: 리스트에서 아직 정렬되지 않은 원소 중 최소인 원소를 **선택**하여 이미 정렬된 부분의 바로 오른쪽 원소와 교환하는 정렬 알고리즘
- 입력에 민감하지 않음 : 어떠한 입력에 대해서도 항상 o(n^2)의 수행시간이 소요됨
- **원소의 위치를 교환하는 최대 횟수**가 n-1번으로 정렬 알고리즘들 중에서 가장 적음
- 원소 비교 횟수 : (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2 = o(n^2)

![image](https://user-images.githubusercontent.com/65997635/128329325-a13906ae-4d08-4e1a-bf37-d470d18599d9.png)


### Insertion Sort ( 삽입 정렬 )
: 리스트가 정렬된 부분과 정렬되지 않은 부분으로 나뉘며, 정렬되지 않은 부분의 가장 왼쪽 원소를 정렬된 부분 중 적절한 위치에 **삽입**하는 방식의 정렬 알고리즘
- 입력에 민감함 
  - 입력이 정렬되어 있는 경우 : 최선의 경우 = n-1회 비교 + 0회 교환 **o(n)**
  - 입력이 역으로 정렬되어 있는 경우 : 최악의 경우 = n(n-1)/2회 비교 + n(n-1)/2회 교환 **o(n^2)**
  - 입력이 임의의 순으로 나열되어 있는 경우 : 평균의 경우 =  0.5 x n(n-1)/2  **o(n^2)**
- 이미 정렬된 데이터에 소량의 신규 데이터를 추가하여 정렬하는 경우 우수한 성능을 보임
- 입력의 사이즈가 작은 경우 우수한 성능을 보임

![image](https://user-images.githubusercontent.com/65997635/128325338-8e941960-0022-4bd1-84c0-3bcbb692bdfc.png)

### Shell Sort ( 셸 정렬 )
: 리스트 내에서 일정한 간격 h로 떨어져 있는 원소끼리 논리적인 sublist를 구성하고, 각 sublist에 있는 원소들에 대해서 **Insertion Sort**을 수행하는 연산을 반복하면서 전체 원소를 정렬하는 알고리즘
- h 정렬 : 간격 h로 떨어져 있는 원소들로 구성된 h개의 서브리스트에 대해서 **Insertion Sort**을 수행하는 알고리즘
  - **( h = 1 )인 경우 = Insertion Sort** : 이미 부분적으로 정렬된 원소들의 수가 많아져서 빠른 속도로 정렬 가능
  - h 정렬은 삽입 정렬을 수행하기 전에 작은 값을 가진 원소들을 리스트 앞부분으로 옮기고, 큰 값을 가진 원소들이 리스트 뒷부분으로 옮기는 전처리 과정임
  - h1 = 내림(n/2), h2 = 내림(h1/2), h3 = 내림(h2/2), ...
- h의 값에 따라 수행 시간이 달라져 분석이 어려움
- 일반적으로 입력 사이즈가 작은 경우 좋은 성능을 보임

![image](https://user-images.githubusercontent.com/65997635/128329203-cd207b5e-8f66-415f-8e8b-25e567bb28a5.png)


🌟 Divide and Conquer 알고리즘
1. 문제 사례를 작은 사례로 분할한다.
2. 작은 사례들을 각각 푼다. 작은 사례가 충분히 작지 않으면 재귀를 사용한다.
3. 작은 사례에 대한 해답을 통합하여 원래 사례의 해답을 구한다.

### Merge Sort ( 합병 정렬 )
:**분할 정복(Divide and Conquer) 알고리즘**
1. 리스트를 두 개의 균등한 크기의 sublist로 분할
2. sublist를 1과 같은 방식으로 모든 sublist의 크기가 1이 될 때까지 재귀적으로 분할
3. n개의 원소를 포함하는 하나의 리스트가 생성될 때까지 sublist를 결합 및 정렬

- 입력에 민감하지 않음
- **정렬 시 추가 메모리 공간이 필요함**
- 자바 객체 정렬에서 시스템 sort로 활용

![image](https://user-images.githubusercontent.com/65997635/128335368-07bbf937-fe22-48a8-9a8a-b041d35b9543.png)

![image](https://user-images.githubusercontent.com/65997635/128333803-580e92c3-196a-4635-a24d-6f36ceb328de.png)

### Quick Sort ( 퀵 정렬 )
:  **분할 정복(Divide and Conquer) 알고리즘**
1. 리스트의 첫 원소를 pivot으로 선택
2. pivot을 기준으로 pivot보다 작은 원소는 pivot의 왼쪽으로, 큰 원소는 pivot의 오른쪽으로 옮겨서 두 개의 sublist 생성
3. pivot을 제외한 왼쪽/오른쪽 sublist에 대해서도 sublist의 사이즈가 0이나 1이 될 때까지 재귀적으로 분할
  - 이때, merge sort와 다르게 quick sort는 분할하면서 정렬함 
4. 정렬된 sublist들 하나의 리스트로 합병

- 입력에 민감함 : 입력의 크기를 n = 2^k라고 가정
  - 최선의 경우 & 평균의 경우 : k(= log n)만큼 분할하며, 각 분할마다 n번의 원소를 비교해야 하므로 o(n log n)
  - 최악의 경우 : 이미 정렬되어 있거나, 역순으로 정렬되어 있다면 n번 분할하며, 각 분할마다 n번의 원소를 비교해야 하므로 o(n^2)
- 평균 시간 복잡도가 o(n log n)인 다른 정렬 알고리즘들보다 빠름
- unix, g++, visual c++ 등에서도 시스템 sort로 사용

![image](https://user-images.githubusercontent.com/65997635/128338303-90f3cff5-4b23-4c59-a8ae-6708201cde6a.png)
![image](https://user-images.githubusercontent.com/65997635/128338313-ecb83880-ead2-431d-b695-19d797a2db3e.png)
![image](https://user-images.githubusercontent.com/65997635/128338324-be829565-3c9d-4538-b9eb-71dd223ce3ee.png)

🌟 Quick sort의 최악의 경우의 시간복잡도를 o(n log n)으로 만드는 법
: pivot으로 median 값을 택한다. 
- median 구하는 법 : 5개씩 나눠서 각각 median을 찾고 이들을 또 5개씩 나눠서 각각 median을 찾는 과정 반복 
-  W(n) = 2 x W(n/2) + c x n이 되어 W(n) = c x(n log n)이 됨

### Heap Sort ( 힙 정렬 )

- 입력에 민감하지 않음
- 입력의 사이즈가 큰 경우 성능이 좋지 않음

#### 방법 1 : 추가 메모리 공간 사용하지 않는 방법
1. 리스트를 Bottom up 방식으로 Max Heap으로 구성 **o(n)**
2. root 노드와 마지막 노드를 교환한 후, heap size를 1 감소시킴 : 가장 큰 수가 정렬됨
3. 노드 교환으로 인해 위배된 힙 속성을 downheap 연산으로 복원 **o(log n)**
4. 2,3 과정을 힙 사이즈가 1이 될 때까지 반복 **n-1번**
→ o(n) + (n-1) x o(log n) = o( n log n )

#### 방법 2 : 추가 메모리 공간을 사용하는 방법
1. 리스트를 Min Heap으로 구성
2. root 노드를 다른 리스트에 저장
3. root 노드를 제외하고 downheap을 통해 힙속성 복원
4. 2,3번을 tree가 empty가 될 때까지 반복

|                | best       | average    | worst      |
|----------------|------------|------------|------------|
| selection sort | o(n^2)     | o(n^2)     | o(n^2)     |
| bubble sort    | o(n^2)     | o(n^2)     | o(n^2)     |
| insertion sort | o(n)       | o(n^2)     | o(n^2)     |
| quick sort     | o(n log n) | o(n log n) | o(n^2)     |
| merge sort     | o(n log n) | o(n log n) | o(n log n) |
| heap sort      | o(n log n) | o(n log n) | o(n log n) |

🌟 Merge sort와 Heap Sort 최악의 경우 시간복잡도가 O(nlogn)이므로 이 둘은 Optimal한 알고리즘임

## Chap 7. Graph
: 연결되어 있는 원소 간의 관계를 표현할 수 있는 자료구조

### Tree와 Graph 관계
: Tree는 연결되어 있고(Connected) 순환하지 않은(Acyclic) 무방향 그래프를 뜻함. 
- 즉, 사이클이 없는 그래프임
- 특히, 계층구조를 이루는 원소 간의 관계를 보이기에 좋음

### 그래프 용어
- G = ( V, E )
- Vertex ( 정점 ) : 연결할 원소
- Edge ( 간선 ) : 정점을 연결하는 역할을 하며, 1개 혹은 2개의 정점을 연결함
- Undirected Graph ( 무방향 그래프 ) : 간선에 방향이 없는 그래프
- Directed Graph ( 방향 그래프 ) : 간선에 방향이 있으므로, 정점들 간의 순서가 중요함
- Degree ( 차수 ) : 특정 정점에 인접한 정점의 수 
  - Adjacent ( 인점 ) : 두 정점이 간선으로 연결되어 있는 경우
  - Directed Graph는 In-degree, out-degree로 구별할 수 있음
- Path ( 경로 ) : 시작 정점부터 도착 정점에 이르기까지의 정점들을 나열한 것
  - Simple Path ( 단순 경로 ) : 경로 상의 정점이 모두 다른 경우
- Cycle ( 싸이클 ) : 시작 정점과 도착 정점이 동일한 Simple Path
- Connected Component : 그래프에서 Vertext들이 서로 연결되어 있는 부분
- Connected Graph ( 연결 그래프 ): Undirected Graph에 있는 모든 정점쌍에 대해서 항상 Path가 존재하는 경우
- Unconnected Graph ( 비연결 그래프 ) : Undirected Graph에서 특정 정점쌍 사이에 Path가 존재하지 않는 경우
- Complete Graph ( 완전 그래프 ) : 그래프에 속해 있는 모든 정점이 서로 연결되어 있는 그래프
  - Undirected Complete Graph의 Vertex 수가 n이면 Edge의 수 = n * (n-1) / 2
- Weighted Graph ( 가중치 그래프 ) : Edge에 가중치가 부여된 그래프로 네트워크라고도 불림
- Subgraph ( 부분 그래프 ) : 주어진 그래프의 일부분인 Vertex와 Edge로 이루어진 집합
- Spanning Tree ( 신장 트리 ) : Connected Graph에서 모든 Vertex들을 Cycle 없이 연결하는 Subgraph

🌟 오일러 경로(Eulerian tour)
: 그래프에 존재하는 모든 Edge을 한 번만 통과하면서 첫 Vertex로 되돌아오는 Path를 뜻함.
- 각각의 Vertex에 연결된 Edge의 개수가 **짝수**일 때만 오일러 경로가 존재함

### 그래프 표현
#### 필요한 이유
- 트리에선 특정 노드 하나(루트 노드)에서 다른 모든 노드로 접근이 가능
- 그래프에선 특정 노드에서 다른 모든 노드로 접근이 가능하지 않음. 따라서, 정보가 필요함

**1. Adjacency Matrix ( 인접 행렬 )

: Vertex 사이에 Edge가 있는지 표현하는 2x2 matrix
- 그래프에 간선이 많이 존재하는 밀집 그래프(Dense Graph) 의 경우
- 장점
  - 두 정점을 연결하는 간선의 존재 여부 (M[i][j])를 O(1) 안에 즉시 알 수 있다.
  - 정점의 차수는 O(N) 안에 알 수 있음 : 인접 배열의 i번째 행 또는 열을 모두 더한다.
- 단점
  - 어떤 노드에 인접한 노드들을 찾기 위해서는 모든 노드를 전부 순회해야 한다.
  - 그래프에 존재하는 모든 간선의 수는 O(N^2) 안에 알 수 있음 : 인접 행렬 전체를 조사한다.
 
**2. Adjacency List ( 인접 리스트 )

: Vertex 마다 인접한 Vertex에 대한 정보를 list나 singly linked list로 표현
- 그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph) 의 경우
- 장점 
  - 어떤 노드에 인접한 노드들을 쉽게 찾을 수 있다.
  - 그래프에 존재하는 모든 간선의 수 는 O(N+E) 안에 알 수 있음 : 인접 리스트 전체를 조사한다.
- 단점
  - 간선의 존재 여부와 정점의 차수 : 정점 i의 리스트에 있는 노드의 수 즉, 정점 차수만큼의 시간이 필요

### 그래프 탐색

**1. Depth First Search ( DFS, 깊이 우선 탐색 )

: 임의의 노드에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 즉, 넓게(wide) 탐색하기 전에 깊게(deep) 탐색하는 것이다.
- 사용하는 경우 : 모든 노드를 방문 하고자 하는 경우에 이 방법을 선택한다.
- 시간 복잡도 : o( Vertex 수 + Edge 수 )

![image](https://user-images.githubusercontent.com/65997635/128386836-a805c426-af58-4f52-9056-2230d1b5738c.png)

**2. Breadth First Search ( BFS, 너비 우선 탐색 )

: 임의의 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법
- 즉, 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것이다.
- 사용하는 경우: 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택한다.
- 시간 복잡도 : o( Vertex 수 + Edge 수 )

![image](https://user-images.githubusercontent.com/65997635/128387001-110ca126-eb85-41bb-9e2c-ec0a347a807d.png)
