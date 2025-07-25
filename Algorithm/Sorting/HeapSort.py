def heapify(arr,n,i):
    largest = i
    left = i*2+1
    right=i*2+2
    
    if left<n and arr[i]<arr[left]:
        largest = left
        
    if right<n and arr[largest]<arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapsort(arr):
    n = len(arr)
    
    for i in range(n//2,-1,-1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
        
arr = [38, 27, 43, 3, 9, 82, 10]
n = len(arr)
print("Unsorted array:", arr)
heapsort(arr)
print("Sorted array:", arr)
        
    