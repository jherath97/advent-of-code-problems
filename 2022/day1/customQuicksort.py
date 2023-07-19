def __partition__(arr, low, high):
    pivot = arr[high][1]
    left = low
    right = high - 1

    while left < right:
        while arr[left][1] < pivot:
            left += 1
        while arr[right][1] > pivot:
            right -= 1
        if left >= right:
            break
        temp0 = arr[left]
        arr[left] = arr[right]
        arr[right] = temp0
    
    temp1 = arr[left]
    arr[left] = arr[high]
    arr[high] = temp1

    return left

def quicksort(arr, low, high):
    if low >= high:
        return
    
    pivotPosition = __partition__(arr, low, high)
    quicksort(arr, low, pivotPosition-1)
    quicksort(arr, pivotPosition+1, high)