def insertion_sort(arr):
    """
    Note: WHEN ARRAY IS ALMOST SORTED THEN IT IS RECOMMEND TO USE INSERTION SORT
    we need to make sub-array in sorted form
    [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    1. [99] -> put 44 in right position in sorted sub array
    2. [44, 99] -> put 6 in right position in sorted sub array
    :param arr:
    :return:
    """
    for i, x in enumerate(arr):
        if i == 0:
            continue
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = (arr[j], arr[i])


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

insertion_sort(arr)
print(arr)
