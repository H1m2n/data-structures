
# Check if a key is present in every segment of size k in an array
# complexity is O(n+k)
def key_check_in_segments(arr, segment_size, key):
    """
    for every segment get the current window size
    if we found a key in a segment then set keys_in_curr_segment to True
    after every segment we need to reset the current window size and keys_in_curr_segment variable
    Time complexity of slicing is O(k)
    :param arr:
    :param segment_size:
    :param key:
    :return:
    """
    keys_in_curr_segment = False
    present_check_list = []
    curr_window_size = len(arr[0:segment_size])
    for i, x in enumerate(arr):
        curr_window_size -= 1
        if x == key:
            keys_in_curr_segment = True
        if curr_window_size == 0:
            curr_window_size = len(arr[i + 1:i + 1 + segment_size])
            present_check_list.append(keys_in_curr_segment)
            keys_in_curr_segment = False

    print(present_check_list)
    return all(ele for ele in present_check_list)


# window size
# arr[0:3]
# arr[3:6]
# arr[6:9]
# arr[9:12]
key_check_in_segments([3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3], 3, 3)
key_check_in_segments([21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25], 5, 23)
key_check_in_segments([5, 8, 7, 12, 14, 3, 9], 2, 8)

# 0, 1, 2, 3, 4, 5
# 0 / 1

# 0, 1, 2, 0, 1, 2
