def max_of_all_sub_array_of_size_k(arr, k):
    i = j = 0
    max_arr = []
    max_e = 0
    while j < len(arr):
        if arr[j] > max_e:
            max_e = arr[j]
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            max_arr.append(max_e)
            i += 1
            j += 1
    return max_arr


arr = [1, 3, -1, -3, 5, 3, 6, 7]
print(max_of_all_sub_array_of_size_k(arr, 3))
