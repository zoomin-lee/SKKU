
#(1)
import random
import time
random.seed(time.time())
a = list()
for _ in range(1000):
    a.append(random.randint(1,1000))
start_time = time.time()
a.sort(reverse = True)
print(time.time()-start_time, "seconds")

#(2) linear search
def linear_search(target, dataset):
    for i in range(len(dataset)):
        if dataset[i] == target:
            return i
    return "NOT found"

dataset = [15,20,30,50,3,40]
result = linear_search(40, dataset)

#(3) 구구단 프로그램
for i in range(1,10):
    for j in range(1,10):
        print(i ,"x", j , "=", i*j, end = ' ')
    print()

# student class
class Student :
    univ = "SKKU" # 클래스 변수 : class의 모든 객체가 공유하는 속성을 위한 변수
    def __init__(self, name, id): # 생성자
        self.name = name # 멤버변수 : 각각의 객체의 속성을 위한 변수
        self.id = id     # 멤버 변수
    def get_name(self):  # 멤버 함수(메소드)
        return self.name
    def get_id(self):    # 멤버 함수(메소드)
        return self.id

#(4) list 이용
assistant = []
num_ass = int(input("input the number of assistant : "))
for i in range(num_ass):
    new_name = input("please enter a name : ")
    new_id = input("please enter a id : ")
    assistant.append(Student(new_name, new_id))
for j in range(num_ass):
    print(j, assistant[j].get_name(), assistant[j].get_id())

#(5) stack 이용
class Stack:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        self.items.pop()

assistant = Stack()
num_ass = int(input("input the number of assistant : "))
for i in range(num_ass):
    new_name = input("please enter a name : ")
    new_id = input("please enter a id : ")
    assistant.push(Student(new_name,new_id))
for j in range(num_ass):
    print(j, assistant.peek().name, assistant.peek().id)
    assistant.pop()

#(6) factorial
def factorial(n): # O(n)
    if n==1 :
        return 1
    else:
        return n * factorial(n-1)

#(7) fibo
def fibo(n): #O(2^n)
    if n<=2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

#(8) binary search
def binary_search(dataset, left, right, target):
    if left > right :
        return "Not found"
    else :
        mid = (left+right)//2
        if dataset[mid] == target :
            return mid
        elif dataset[mid] > target :
            binary_search(dataset, left, mid-1, target)
        else:
            binary_search(dataset, mid+1, right, target)
