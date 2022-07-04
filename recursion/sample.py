# def regress(i):
#     print(i)
#     if i <= 1:
#         return
#     else:
#         regress(i-1)


# def su(arr):
#     if not arr:
#         return 0
#     return arr[0] + su(arr[1:])


# def counter(arr):
    
#     if not arr:
#         return 0
#     else:
#         return 1 + counter(arr[1:])

# def high(arr):

#     if len(arr) == 2:
#         if arr[0] > arr[1]:
#             return arr[0]
#         else: 
#             return arr[1]

#     sub = high(arr[1:])
#     if arr[0] > sub:
#         return arr[0]
#     else:
#         return sub

# def vertical(n):
#     if n < 10:              # base case: n has one number
#         print(n)            
#     else:
#         vertical(n // 10)   # show everthing numbers except the last
#         print(n % 10)       # show the last number of n

# def reverse(n):
#     if n < 10:
#         print(n)
#     else:
#         print(n % 10)
#         reverse(n // 10)


# def cheers(n):
#     if n == 0:
#         print('Hurrah')
#     else:
#         print('Hip', end=' ')
#         return cheers(n - 1)


def fat(n):
    if n in [0, 1]:
        return 1
    elif n > 1:
        return n * fat(n-1)
    return None


# l = [1, 2, 4, 6, 7]
# print(regress(9))
# print(su(l))
# print(counter(l))
# print(high(l))
# vertical(10)
# reverse(3124)
# cheers(3)
print(fat(5))