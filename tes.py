def som(arr):
    if not arr:
        return 0
    else:
        return arr[0] + som(arr[1:])


def maior(arr):

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    
    sub = maior(arr[1:])
    if arr[0] > sub:
        return arr[0]
    else:
        return sub


def count(arr):
    if not arr:
        return 0
    else:
        return 1 + count(arr[1:])


def fat(num):
    if num == 1:
        return 1
    else:
        return num * fat(num - 1)


# print(som([2,3,5]))
# print(maior([78, 5, 1, 340]))
print(count([2, 45, 4, 6, 34, 3]))
print(fat(5))
