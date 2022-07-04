#  Book example:
#  def quicksort(arr):
    #  if len(arr) < 2:
        #  return arr
    #  else:
        #  pivot = arr[0]
        #  sub_low = [i for i in arr[1:] if i <= pivot]
        #  sub_high = [i for i in arr[1:] if i > pivot]
        #  return quicksort(sub_low) + [pivot] + quicksort(sub_high)


#  Yt example:
def quick_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1 # The last item
    if begin < end:
         p = partition(arr, begin, end)
         quick_sort(arr, begin, p-1) # Sub array, left size of pivot
         quick_sort(arr, p+1, end) # Sub array, right size of pivot
    return arr

def partition(arr, begin, end): # Begin get 
    pivot = arr[end]  # in this case pivot is the last element
    i = begin
    for j in range(begin, end):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


#  Another video
#  def quicksort(arr, left, right):
    #  if left < right:
        #  part = particion(arr, left, right)
        #  quicksort(arr, left, part-1)
        #  quicksort(arr, part+1, right)

#  def particion(arr, left, right):
    #  i = left
    #  j = right - 1
    #  pivot = arr[right]

    #  while i < j:
        #  while i < right and arr[i] < pivot:
            #  i += 1
        #  while j > left and arr[j] >= pivot:
            #  j -= 1
        #  if i < j:
            #  arr[i], arr[j] = arr[j], arr[i]

    #  if arr[i] > pivot:
        #  arr[i], arr[right] = arr[right], arr[i]

    #  return i


ar = [43, 3, 12, 1, 76, 8]
quicksort(ar, 0, len(ar) - 1)
print(ar)
