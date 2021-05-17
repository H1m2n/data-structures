# Complexity O(n log n) As here we are not comparing a element with each
# instead we are generating 2 sorted array in each recursion and making one array by just comparing log n time
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    divide_index = len(arr) // 2
    left_arr = arr[0:divide_index]
    right_arr = arr[divide_index:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return compare(
        left_arr,
        right_arr
    )


def compare(left_arr, right_arr):
    print('-------------------------')
    print('left arr - {}'.format(left_arr))
    print('right arr - {}'.format(right_arr))
    merged_arr = []
    left_i, right_i = (0, 0)
    max_left_i = len(left_arr) - 1
    max_right_i = len(right_arr) - 1
    while True:
        if left_arr[left_i] < right_arr[right_i]:
            merged_arr.append(left_arr[left_i])
            left_i += 1
        else:
            merged_arr.append(right_arr[right_i])
            right_i += 1
        if left_i >= max_left_i or right_i > max_right_i:
            break
    merged_arr.extend(left_arr[left_i:])
    merged_arr.extend(right_arr[right_i:])
    print(merged_arr)
    return merged_arr


a = [3, 4, 1, 2, 7, 5, 6, 8]
print(merge_sort(a))
