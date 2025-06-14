def bubbleSort(arr, n):
    for _ in range(n):
        for j in range(0, n - 2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
print("Unsorted array:", arr)

sorted_arr = bubbleSort(arr, n)
print("Sorted array:", sorted_arr)
