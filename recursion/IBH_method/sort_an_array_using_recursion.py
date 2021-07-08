arr = [0, 5, 1, 2]


# o/p -> [0, 1, 2, 5]

# hypothesis for sort
# we are guranteed that a function we design will give me expected result
# that function is sort, we just take care of induction step

# sort(n-1) and push back the popped element to its right position

def insert(sorted_arr, val):
    # sorted_arr = [0, 1, 5]  val = 2
    # we need to push val in its correct position in sorted array
    if len(sorted_arr) == 0 or sorted_arr[-1] <= val:
        # on smaller input array will be shorter and shorter
        # so at some point array will be empty or the last element of the array will be smaller than than the value, so
        # in this case we simply append that value in list
        sorted_arr.append(val)
        return

    last_ele = sorted_arr[-1]
    sorted_arr.pop()
    insert(sorted_arr, val)
    # arr = [0, 1], val = 2, popped element = 5
    # from hypothesis step we will expect that we get the value to be inserted at its correct position, we just
    # take care of the induction step to put value back in expected array from hypothesis step
    sorted_arr.append(last_ele)


arr1 = [1, 2, 3, 4, 5]
val = 0
insert(arr1, val)
print(arr1)

arr2 = [1, 2, 4, 5]
val = 3
insert(arr2, val)
print(arr2)


def do_sort(arr, last_index):
    if not arr:
        return

    last_ele = arr[last_index]
    arr.pop()
    do_sort(arr, len(arr) - 1)
    # from previous hypothesis step we will expceted arr = [0, 1, 5] the last element (2) that we have removed from array
    # that we need to place on right position of the sorted array
    insert(arr, last_ele)


def sort_arr(arr):
    do_sort(arr, len(arr) - 1)


sort_arr(arr)
print(arr)

arr3 = [10, 20, 2, 100, 40, 30, 5, 1]
sort_arr(arr3)
print(arr3)
