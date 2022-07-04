# Binary Search
def binary(arr, item, begin=0, end=None):
    if end is None:
        end = len(arr) - 1

    if begin <= end:
        mid = (begin + end) // 2
        
        if arr[mid] == item:
            return mid
        if item < arr[mid]:
            return binary(arr, item, begin, mid - 1)
        else:
            return binary(arr, item, mid + 1, end)

    return None


# Selection Sort
def selection(arr):

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


# Recursion
def high(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    sub_array = high(arr[1:])
    if arr[0] > sub_array:
        return arr[0]
    else:   
        return sub_array
    
def pattern(n):
    if n == 0:
        print('>>>')
    elif n > 0:
        pattern(n - 1) 
        print(n * '*')
        return pattern(n - 1)

def fat(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fat(n - 1)


# QuickSort
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
    for j in range(left, right):  # j: step
        if arr[j] <= pivot:  # if numerber in index j on arr
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


# print('Binary and Sort Selection')
lisa = [23, 67, 23, 3, 34, 78, 2, 43, 45, 86, 234, 7]
# print('\n',binary(selection(lisa), 78))
# print(selection(lisa))
# print(high(lisa))
# pattern(3)
# print(fat(0))
print(quicksort(lisa))
