def find_higher(arr, num, left=0, right=None):    
    if right==None:
        right = len(arr) - 1
    mid = (left + right) // 2
    if left <= right:
        if arr[mid] >= num:
            return find_higher(arr, num, left, mid-1)
        else:
            return find_higher(arr, num, mid+1, right)
    return arr[mid+1]


lista = [1, 3, 5, 9, 13, 17, 19, 20, 23, 24]
print(find_higher(lista, 4))
print(find_higher(lista, 11))
print(find_higher(lista, 22))
