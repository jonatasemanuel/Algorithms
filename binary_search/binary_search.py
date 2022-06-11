def binary_search(numbers_list, find, begin=0, end=None):
    """
    This function aim to a binary search, that is, instead of searching index by
    index as in linear search, the search is done in half of the list, and thus
    reducing until finding the number.

    Args:
        numbers_list (list): Here is the sorted list with the numbers.
        find (int): The number to search.
        begin (int): Here is the first index(number) of the search. Defaults to 0.
        end (bool): Here is the last index(number) of the search. Defaults to None.

    Returns:
        int : if the number is in the list.
        str : if the number is not found.
    """
    if end is None:
        end = len(numbers_list) - 1
    
    if begin <= end:
        mid = (begin + end) // 2

        if numbers_list[mid] == find:
            return mid
        if find < numbers_list[mid]:
            return binary_search(numbers_list, find, begin, mid-1)
        else:
            return binary_search(numbers_list, find, mid+1, end)

    return 'Not found'


numbers = [2, 3, 5, 6, 8, 9, 12, 17, 19, 20, 13]
print()
print('Index: ', binary_search(numbers, 1))
print('Index: ', binary_search(numbers, 20))
