def get_max(arr):
    max_ele = arr[0]
    for x in arr:
        if x > max_ele:
            max_ele = x
    return max_ele


def get_min(arr):
    min_ele = arr[0]
    for x in arr:
        if x < min_ele:
            min_ele = x
    return min_ele


def min_max_ele_in_arr(arr):
    min_ele = get_min(arr)
    max_ele = get_max(arr)
    return (min_ele, max_ele)


print(min_max_ele_in_arr([0, 1, 2, 3]))
