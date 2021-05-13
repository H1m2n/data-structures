# Complexity O(n log n) As here we are not comparing a element with each
# instead we are generating 2 sorted array in each recursion and just comparing log n time
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    divide_index = len(arr) // 2
    left_arr = arr[0:divide_index]
    right_arr = arr[divide_index:]
    return compare(
        merge_sort(left_arr),
        merge_sort(right_arr)
    )


def compare(left_arr, right_arr):
    print('-------------------------')
    print('left arr - {}'.format(left_arr))
    print('right arr - {}'.format(right_arr))
    merged_arr = []
    left_i, right_i = (0, 0)
    while left_i < len(left_arr) and right_i < len(right_arr):
        if left_arr[left_i] < right_arr[right_i]:
            merged_arr.append(left_arr[left_i])
            left_i += 1
        else:
            merged_arr.append(right_arr[right_i])
            right_i += 1
    merged_arr.extend(left_arr[left_i:])
    merged_arr.extend(right_arr[right_i:])
    print(merged_arr)
    return merged_arr


a = [3, 4, 1, 2, 7, 5, 6, 8]
print(merge_sort(a))
