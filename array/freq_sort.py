def freq_sort():
    arr = [2, 3, 1, 3, 2]

    freq_map = {}
    for x in arr:
        if x in freq_map:
            freq_map[x] = freq_map[x] + 1
        else:
            freq_map[x] = 1
    tuple_list = list(freq_map.items())
    # we need to sort increasing order of freq(2nd ele in tuple) and decreasing order of number(1st ele in tuple)
    sorted_tuple_list = sorted(tuple_list, key=lambda sub: (sub[1], -sub[0]))
    res = []
    for x in sorted_tuple_list:
        n = x[1]
        while n > 0:
            res.append(x[0])
            n -= 1

    # tuple_list.sort(key=custom_sort)
    # res = sorted(tuple_list, key=custom_sort)
    print(res)


freq_sort()
