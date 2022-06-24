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



# print('Binary and Sort Selection')
# lisa = [23, 67, 23, 3, 34, 78, 2, 43, 45, 86, 234, 7]
# print('\n',binary(selection(lisa), 78))
# print(selection(lisa))
