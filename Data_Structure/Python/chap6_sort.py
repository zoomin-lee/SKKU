
def selection_sort(items):
    for i in range(0,len(items)-1):
        minimum = i
        for j in range(i, len(items)):
            if items[minimum] > items[j]:
                minimum=j
        items[i], items[minimum] = items[minimum], items[i]

items = [40,10,70,30]
print("\n선택 정렬 전 : ", items)
selection_sort(items)
print("선택 정렬 후 : ", items)

def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j-1] > items[j]:
                items[j], items[j-1] = items[j-1], items[j]
            else :
                break

items = [40,10,20,50,70,30,90]
print("\n삽입 정렬 전 : ", items)
insertion_sort(items)
print("삽입 정렬 후 : ", items)

def bubble_sort(items):
    n = len(items)-1
    for i in range(n, 0, -1):
        for j in range(0, i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

items = [40,10,20,50,70,30,90]
print("\n버블 정렬 전 : ", items)
bubble_sort(items)
print("버블 정렬 후 : ", items)

def shell_sort(items):
    h = len(items) // 2
    while h >= 1:
        for i in range(h, len(items)):
            j = i
            while j >=h and items[j] < items[j-h]:
                items[j], items[j - h] = items[j - h], items[j]
                j -=h
        print(h, "- 정렬 결과 : ", items)
        h //= 2

items = [40,10,20,50,70,30,90]
print("\n셸 정렬 전 : ", items)
shell_sort(items)
print("셸 정렬 후 : ", items)

def downheap(i, size):
    while 2 * i + 1 <= size:
        k = 2 * i +1
        if k < size -1 and items[k] < items[k+1]:
            k += 1
        if items[i] >= items[k]:
            break
        items[i] ,items[k] = items[k], items[i]
        i = k

def heapify(items):
    hsize = len(items)
    for i in range(hsize//2 - 1, -1, -1):
        downheap(i, hsize)

def heap_sort(items):
    N = len(items)
    for i in range(N):
        items[0], items[N-1] = items[N-1], items[0]
        downheap(0, N-2)
        N-=1

items = [40,10,20,50,70,30,90]
print("\n힙 정렬 전 : ", items)
heapify(items)
print("Max heap만들기 : ", items)
heap_sort(items)
print("힙 정렬 후 : ", items)


def merge(items, temp, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i > mid:
            temp[k] = items[j]
            j +=1
        elif j > high:
            temp[k] = items[i]
            i +=1
        elif items[j] < items[i]:
            temp[k] = items[j]
            j +=1
        else :
            temp[k] = items[i]
            i +=1
    for k in range(low, high+1):
        items[k] = temp[k]

def merge_sort(items, temp, low, high):
    if high <= low:
        return None
    mid = low + (high-low)//2
    merge_sort(items, temp, low, mid)
    merge_sort(items, temp, mid+1, high)
    merge(items, temp, low, mid, high)

items = [40,10,20,50,70,30,90]
temp =[None]*len(items)
print("\n합병 정렬 전 : ", items)
merge_sort(items, temp, 0, len(items)-1)
print("합병 정렬 후 : ", items)

def partition(items, pivot, high):
    i = pivot +1
    j = high
    while True:
        while i < high and items[i] < items[pivot]:
            i += 1
        while j > pivot and items[j] > items[pivot]:
            j -= 1
        if j <= i:
            break
        items[i], items[j] = items[j], items[i]
        i += 1
        j -= 1
    items[pivot], items[j] = items[j], items[pivot]
    return j

def quick_sort(items, low, high):
    if low<high:
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot-1)
        quick_sort(items, pivot+1, high)

items = [40,10,20,50,70,30,90]
print("\n퀵 정렬 전 : ", items)
quick_sort(items, 0, len(items)-1)
print("퀵 정렬 후 : ", items)