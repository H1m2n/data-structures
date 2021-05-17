def max_sum_subarray_of_size_k(arr, k):
    if k > len(arr):
        return sum(arr)

    max_sum = e_sum = 0
    i = j = 0
    while j < len(arr):
        window_size = j - i + 1
        # print(window_size, i, j)
        e_sum = e_sum + arr[j]
        if window_size < k:
            # if window size is less, then simply we need to increment j++
            j += 1
        elif window_size == k:
            # get the max sum when we hit the window size
            max_sum = max(max_sum, e_sum)
            # now we need to maintain window as we already hit the window size
            # so we can increment i++ and j++ but before doing this we need to
            # exclude arr[i] from e_sum
            e_sum = e_sum - arr[i]
            i += 1
            j += 1
    return max_sum


arr = [1, 2, 5, 4, 3, 2, 1]
max_sum = max_sum_subarray_of_size_k(arr, 1)
print(max_sum)

max_sum = max_sum_subarray_of_size_k(arr, 2)
print(max_sum)

max_sum = max_sum_subarray_of_size_k(arr, 8)
print(max_sum)
