import sys
a = int(input())
arr = [int(sys.stdin.readline()) for _ in range(a)]

def heapify(arr, idx, size):
    left = idx*2+1
    right = idx*2+2
    largest = idx

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr, largest, size)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

heap_sort(arr)

for i in arr:
    print(i)