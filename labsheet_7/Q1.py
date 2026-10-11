import heapq

min_heap=[]

arr=[4,2,7,1,3,5]

for x in arr:

    heapq.heappush(min_heap,x)
print("Min Heap:",min_heap)

print("Priority Queue:",end=" ")

while min_heap:
    print(heapq.heappop(min_heap),end=" ")
max_heap=[]

for x in arr:
    heapq.heappush(max_heap,-x)
print("\nMax Heap:",[-x for x in max_heap])
print("Priority Queue:",end=" ")

while max_heap:
    print(-heapq.heappop(max_heap),end=" ")

def heap_sort(arr):
    heap=[]
    for x in arr:
        heapq.heappush(heap,x)
    result=[]
    while heap:
        result.append(heapq.heappop(heap))
    return result
arr=[4,2,7,1,3,5]
print("\nOriginal Array:",arr)
print("Heap Sort:",heap_sort(arr))