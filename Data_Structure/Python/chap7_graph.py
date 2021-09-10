
class Node :
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
            temp.next = temp
        else :
            temp.next = self.head.next
            self.head.next=temp
            self.head=temp

    def dequeue(self):
        if self.is_empty():
            return None
        else :
            temp = self.head.next
            if temp == temp.next:
                self.head = None
            else :
                self.head.next = temp.next
        return temp.item

# DFS : 깊이우선탐색
adj_list =[[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [False] * N

def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)

print("DFS 방문 순서 : ")
for i in range(N):
    if not visited[i]:
        dfs(i)

# BFS : 너비우선탐색
def bfs(v): #o(간선+정점)
    queue = Queue()
    visited[v] = True
    queue.enqueue(v)

    while not queue.is_empty():
        v = queue.dequeue()
        print(v, ' ', end='')
        for i in adj_list[v]:
            if not visited[i]:
                visited[i] = True
                queue.enqueue(i)

adj_list =[[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [False] * N

print("\nBFS 방문 순서 : ")
for i in range(N):
    if not visited[i]:
        bfs(i)