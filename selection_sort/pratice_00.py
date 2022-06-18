def selection_sort(arr):

    for ord in range(len(arr) - 1):
        min_index = ord
        for item in range(ord, len(arr)):
            if arr[item] < arr[min_index]:
                min_index = item

        if arr[ord] > arr[min_index]:
            aux = arr[ord]
            arr[ord] = arr[min_index]
            arr[min_index] = aux

    return arr


lista = [7, 5, 1, 8, 3]
lista2 = [7, 5, 435, -56, 0]
lista3 = ['jon', 'abrahan', 'camile', 'jacob', 'phill']
print(selection_sort(lista))
print(selection_sort(lista2))
print('\n',selection_sort(lista3))