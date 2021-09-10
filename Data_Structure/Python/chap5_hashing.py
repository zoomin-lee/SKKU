
class LinearProbing:
    def __init__(self, size):
        self.m = size
        self.k = [None for _ in range(size+1)] # 키 값 저장
        self.d = [None for _ in range(size+1)] # 데이터 값 저장

    def hash(self, key): # 키 값을 해쉬 값으로 변환
        return key % self.m

    def insert(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.k[i] == None or self.k[i] == '$': # 빈 슬롯
                self.k[i] = key
                self.d[i] = data
                return None
            if self.k[i] == key: # 삽입하고자 하는 키 값이 존재한다면 데이터 값만 바꿈
                self.d[i] = data
                return None
            # 충돌 발생
            j += 1
            i = ( initial_position + j ) % self.m # 다음 while 루프에서 방문할 슬롯의 위치 결정
            if i == initial_position : # 빈 슬롯이 없으므로 삽입 실패
                break

    def search(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None:
            if self.k[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position +j) % self.m
            if i == initial_position: # 검색 실패
                break
        return None

    def delete(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None:
            if self.k[i] == key:
                self.k[i] = '$'
                self.d[i] = None
                return None
            j += 1
            i =(initial_position +j) % self.m
            if i == initial_position:
                break
        return None

    def print_table(self):
        for i in range(self.m) : print("%-6d" %i , end ='')
        print()
        for i in range(self.m):
            if type(self.k[i]) == int : print("%-6d" %self.k[i], end='')
            elif self.k[i] == "$" : print("$     ", end='')
            else : print(self.k[i], end='  ')
        print()
        for i in range(self.m):
            if type(self.d[i]) == str : print(self.d[i], end='     ')
            else : print(self.d[i], end='  ')

class Node :
    def __init__(self, key, data, link):
        self.key = key      # key field : 데이터의 키 값을 저장
        self.data = data    # data field : 데이터 값을 저장
        self.next = link    # link field : 다음 순서 노드의 참조를 저장( 데이터를 노드로 저장 )

class Chaining :
    def __init__(self, size):
        self.m = size
        self.table = [None for x in range(size+1)]
        # 해시 테이블의 각 항목 table[i]는 해시 값 i를 가지는 데이터들을 저장하는 노드들의 연결리스트의 첫 노드를 가리키는 head 역할을 함

    def hash(self, key):
        return key % self.m

    def insert(self, key, data):
        i = self.hash(key)
        p = self.table[i]
        while p != None :
            if key == p.key:
                p.data = data
                return None
            p = p.next
        self.table[i] = Node(key, data, self.table[i]) # link list 맨 앞에 삽입 o(1)

    def search(self, key):
        i = self.hash(key)
        p = self.table[i]
        while p != None:
            if key == p.key:
                return p.data
            p = p.next
        return None

    def delete(self, key):
        i = self.hash(key)
        p = self.table[i]
        previous = None
        while p != None:
            if key == p.key:
                if previous == None: # 첫 노드가 delete할 값인 경우
                    self.table[i] = p.next
                else :
                    previous.next = p.next
                return None
            previous = p
            p = p.next

    def print_table(self):
        for i in range(self.m):
            print("%2d" %i, end='')
            if self.table[i] != None:
                p = self.table[i]
                while p != None:
                    print(" --> [", p.key, ",", p.data,"]", end='')
                    p = p.next
            print()

if __name__ == '__main__':
    # ht = LinearProbing(13)
    # ht.insert(45,'A')
    # ht.insert(27,'B')
    # ht.insert(88,'C')
    # ht.insert(9,'D')
    # ht.insert(71,'E')
    # ht.insert(60,'F')
    # ht.insert(46,'G')
    # ht.insert(38,'H')
    # ht.insert(24,'I')
    #
    # print("######### 선형 조사 방법 ########")
    # print("해시 테이블 : ")
    # ht.print_table()
    # print()
    # print("\nkey 값이 46인 data 검색 결과 : ", ht.search(46))
    # ht.delete(60)
    # ht.delete(46)
    # print("\nkey 값이 60인 F 삭제 후, key 값이 46인 G를 삭제한 해시 테이블 : ")
    # ht.print_table()

    ht = Chaining(13)
    ht.insert(45, 'A')
    ht.insert(27, 'B')
    ht.insert(88, 'C')
    ht.insert(9, 'D')
    ht.insert(71, 'E')
    ht.insert(60, 'F')
    ht.insert(46, 'G')
    ht.insert(38, 'H')
    ht.insert(24, 'I')

    print("######### 체이싱 방법 ##########")
    print("해시 테이블 : ")
    ht.print_table()
    print()
    print("key 값이 9인 data 검색 결과 : ", ht.search(9))
    ht.delete(71)
    ht.delete(45)
    print("\nkey 값이 71인 E 삭제 후, key 값이 45인 A를 삭제한 해시 테이블 : ")
    ht.print_table()