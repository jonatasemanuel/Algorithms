def binary_search(arr, item, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == item:
            return mid
        if item < arr[mid]:
            return binary_search(arr, item, left, mid-1)
        else:
            return binary_search(arr, item, mid+1, right)
    return None


def selection_sort(arr):
    for item in range(len(arr) - 1):
        min_index = item
        for min in range(item, len(arr)):
            if arr[min] < arr[min_index]:
                min_index = min
 
        if arr[item] > arr[min_index]:
            aux = arr[item]
            arr[item] = arr[min_index]
            arr[min_index] = aux

    return arr


def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


lis = [999, 32, 764, 3, 232, 6, 65, 734, 1]
#  quicksort(lis)
#  print(lis)
#  print(binary_search(lis, 764))
selection_sort(lis)
print(lis)
