def sort(arr, pivot_index, expected_compares):
    # [6, 4, 1, 2, 10, 7, 5]
    # [7, 4, 1, 2, 10, 5, 6]
    # [10, 4, 1, 2, 5, 7, 6]
    # [2, 4, 1, 5, 10, 7, 6]
    # [2, 4, 1, 5, 10, 7, 6]
    if len(arr) == 1:
        return arr
    pivot_no = arr[pivot_index]
    (i, j) = (0, pivot_index)
    no_of_compares = 0
    while no_of_compares <= expected_compares:
        compare_no = arr[i]
        if compare_no > pivot_no:
            tmp = arr[i]
            arr[i] = arr[j - 1]
            arr[j - 1] = pivot_no
            arr[j] = tmp
            j -= 1
        else:
            i += 1
        no_of_compares += 1
        print(arr)
    pivot_no_index = j
    return arr, pivot_no_index


# input_arr = [6, 4, 1, 2, 10, 7, 5]
input_arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
# arr, i = sort(input_arr, -1, 8)
# print("{} -> {}".format(arr, i))

# arr, i = sort(input_arr, -6, 2)
# print("{} -> {}".format(arr, i))

# arr, i = sort(input_arr, -6, 2)
# print("{} -> {}".format(arr, i))
