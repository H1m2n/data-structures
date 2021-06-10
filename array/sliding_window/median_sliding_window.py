# if k is odd -> median can be found at (k // 2)th index
# if k is even -> median can be found at k // 2 = i, so median will be (arr[i-1] + arr[i]) / 2


def median_sliding_window(nums, k):
    # check if k is even or odd
    if k % 2 == 0:
        # k is even
        if k == 2:
            median_index_1, median_index_2 = (0, 1)
        else:
            median_index_1, median_index_2 = ((k // 2) - 1, k // 2)
    else:
        # k is odd
        if k == 1:
            median_index_1, median_index_2 = (0, 0)
        else:
            median_index_1, median_index_2 = (k // 2, k // 2)

    i, j = (0, 0)
    median_arr, arr = ([], [])
    while j < len(nums):
        arr.append(nums[j])
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            # sort the array
            sort_arr = sorted(arr[i:i + k])
            # find median in sorted array
            median = (sort_arr[median_index_1] + sort_arr[median_index_2]) / 2
            median_arr.append(median)
            i += 1
            j += 1
    return median_arr


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
nums = [1, 4, 2, 3]
k = 4
nums = [1]
k = 1
print(median_sliding_window(nums, k))
