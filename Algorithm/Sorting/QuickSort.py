def partion(arr, l, h):
    pivot = arr[l]
    i = l
    j = h
    while i < j:
        while arr[i] <= pivot and i < h:
            i += 1
        while arr[j] > pivot and j > l:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quicksort(arr, l, h):
    if l < h:
        j = partion(arr, l, h)
        quicksort(arr, l, j)
        quicksort(arr, j + 1, h)


arr = [38, 27, 43, 3, 9, 82, 10]
n = len(arr)
print("Unsorted array:", arr)
quicksort(arr, 0, n - 1)
print("Sorted array:", arr)