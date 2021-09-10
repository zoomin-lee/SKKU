

# 정렬된 리스트
class list_priorityqueue :
    def __init__(self):
        self.priority_list = []

    def enqueue(self, item):
        index = 0
        for i in range(len(self.priority_list)):
            if self.priority_list[i] < item:
                index = i+1
        self.priority_list.insert(index, item)

    def dequeue(self):
        self.priority_list.pop()

    def print_list(self):
        print(self.priority_list)

# 정렬된 단순 연결 리스트 : 작을수록 우선순위가 높다면 오름차순
class Node:
    def __init__(self, item):
        self.key = item
        self.next = None

class linked_PriorityQueue :
    def __init__(self):
        self.head = None

    def enqueue(self, item): #탐색 o(n)+ 삽입 o(1)
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.item > item:
                stop = True
            else :
                previous = current
                current = current.next
        temp = Node(item)

        if previous == None:
            temp.next = self.head
            self.head = temp
        else :
            temp.next = current
            previous.next = temp

    def dequeue(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            dequeue_item = temp.item
            self.head = self.head.next
            return dequeue_item

# 환형연결리스트로 구현
class CList_priorityqueue :
    def __init__(self):
        self.head = None # 마지막 노드

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.next = temp
            self.head = temp
        else:
            temp.next = self.head.next
            self.head.next = temp

    def dequeue(self):
        temp = self.head.next
        current = temp
        max = current.key
        while True :
            if max < current.next.key:
                max = current.next.key
                delete_node = current.next
                previous = current
            current = current.next
            if current != temp :
                continue
            else :
                previous.next = delete_node.next
                break

    def print_list(self):
        temp = self.head.next
        current = temp
        while True:
            print(current.key, end=' ')
            current = current.next
            if current != temp:
                continue
            else:
                break
        print()

# Min heap
class Binaryminheap :
    def __init__(self, array=[]): # o(1)
        self.items = array

    def size(self): # o(1)
        return len(self.items)

    def swap(self, i, j): # o(1)
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self,key): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 upheap
        self.items.append(key)
        self.upheap(self.size()-1)

    def extract_min(self): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 downheap
        if self.size() == 0:
            print("heap is empty")
            return None
        minimum = self.items[0]
        self.swap(0,-1)
        del self.items[-1]
        self.downheap(0)
        return minimum

    def downheap(self, i):
        while 2*i + 1 <= self.size()-1:
            k = 2*i+1
            if k < self.size()-1 and self.items[k] > self.items[k+1]:
                k += 1
            if self.items[i] < self.items[k]:
                break
            self.swap(i, k)
            i = k

    def upheap(self, i):
        while i > 0 and self.items[(i-1//2)] < self.items[i]:
            self.swap(i, (i-1)//2)
            i = (i-1) // 2

    def heapify(self, array): #o(n)
        for i in range(len(array)//2-1, -1, -1):
            self.downheap(i)

    def print_heap(self):
        for i in range(0,self.size()):
            print(self.items[i], end = ' ')
        print("\nsize of heap = ", self.size())

# Max heap
class Binarymaxheap :
    def __init__(self, array=[]): # o(1)
        self.items = array

    def size(self): # o(1)
        return len(self.items)

    def swap(self, i, j): # o(1)
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self,key): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 upheap
        self.items.append(key)
        self.upheap(self.size()-1)

    def extract_max(self): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 downheap
        if self.size() == 0:
            print("heap is empty")
            return None
        maxmum = self.items[0]
        self.swap(0,-1)
        del self.items[-1]
        self.downheap(0)
        return maxmum

    def downheap(self, i):
        while 2*i + 1 <= self.size()-1:
            k = 2*i+1
            if k < self.size()-1 and self.items[k] < self.items[k+1]:
                k += 1
            if self.items[i] > self.items[k]:
                break
            self.swap(i, k)
            i = k

    def upheap(self, i):
        while i > 0 :
            parent_index = (i-1) // 2
            if self.items[parent_index] < self.items[i] :
                self.swap(i, (i-1)//2)
                i = (i-1) // 2
            else :
                break

    def heapify(self, array): #o(n)
        for i in range(len(array)//2-1, -1, -1):
            self.downheap(i)

    def print_heap(self):
        for i in range(0,self.size()):
            print(self.items[i], end = ' ')
        print("\nsize of heap = ", self.size())

if __name__ == '__main__':
    array = [3,2,4,9,5,8,6]
    minheap = Binarymaxheap(array)
    minheap.heapify(array)
    minheap.print_heap()
    minheap.insert(11)
    minheap.print_heap()
    minheap.insert(10)
    minheap.print_heap()
    print(minheap.extract_max())
    minheap.print_heap()
