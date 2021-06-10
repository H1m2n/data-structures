# 
from collections import defaultdict


def min_window_substr(s, t):
    pattern_map = defaultdict(lambda: 0)
    for x in t:
        pattern_map[x] = pattern_map[x] + 1
    distinct_char_count = len(pattern_map)
    # print(pattern_map)

    min_i, min_j = (0, 0)
    i = j = 0
    min_l = 0
    while j < len(s):
        if s[j] in pattern_map:
            pattern_map[s[j]] = pattern_map[s[j]] - 1
            if pattern_map[s[j]] == 0:
                distinct_char_count -= 1

        # print(i, j, pattern_map, distinct_char_count)
        if distinct_char_count > 0:
            j += 1
        elif distinct_char_count == 0:
            # we have expanded right pointer to meet the condition
            # now our job is to make window as shrink as possible while satisfying the condition
            while distinct_char_count == 0:
                if s[i] in pattern_map:
                    pattern_map[s[i]] = pattern_map[s[i]] + 1
                    if pattern_map[s[i]] == 1:
                        distinct_char_count += 1
                i += 1
            window_size = j - (i - 1) + 1
            if min_l == 0:
                min_l = window_size
                min_i = i - 1
                min_j = j
            else:
                if window_size < min_l:
                    min_i = i - 1
                    min_j = j
                min_l = min(min_l, window_size)
            j += 1
    print(min_l, min_i, min_j)
    if min_l == 0:
        return ""
    else:
        return s[min_i:min_j + 1]


s = "ADOBECODEBANC"
# s = "ADOBECAODEBANC"
# s = "ADOBECA"
# s = 'ABC'
t = "ABC"
s = "a"
t = "a"
print(tmp(s, t))
# {
#     a: -1, 0
#     b: 0,
#     c: 0,
# }
