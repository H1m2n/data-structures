def get_intersection(arr1, arr2):
    """
    convert one of the array in map
    compare array element with map that found commonly put that into set
    :param arr1:
    :param arr2:
    :return:
    """
    arr_map = {}
    for x in arr1:
        arr_map[x] = 1

    common_set = set()
    for x in arr2:
        if arr_map.get(x) and x not in common_set:
            common_set.add(x)
    print(common_set)
    return common_set


def get_union(arr1, arr2):
    """
    convert one of the array in map
    compare array element with map that found commonly put that into set and update flag in map to 0
    after all iteration put all map element to set that has flag 1
    :param arr1:
    :param arr2:
    :return:
    """
    arr_map = {}
    for x in arr1:
        arr_map[x] = 1

    union_set = set()
    for x in arr2:
        if arr_map.get(x) and x not in union_set:
            arr_map[x] = 0
        union_set.add(x)

    for x, f in arr_map.items():
        if f == 1:
            union_set.add(x)
    print(union_set)
    return union_set


get_intersection([1, 3, 4, 5, 7], [2, 3, 5, 6, 3])

get_union([1, 3, 4, 5, 7], [2, 3, 5, 6, 3])
