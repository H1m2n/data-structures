"""
str = abcbdbdbbdcdabd
For k = 2, o/p is ‘bdbdbbd’ -> contains 2 distinct character
For k = 3, o/p is ‘bcbdbdbbdcd’ -> contains 3 distinct character
For k = 4, o/p is ‘abcbdbdbbdcdabd’ -> contains 4 distinct character
"""

# approach -->
# create a map of uniq character
# whenever we encounter distinct char count > k, we should move i until we don't encounter 0 for first character in map
# then this cycle goes on
from collections import defaultdict


def longest_substr_of_k_distinct_char(str, k):
    i = j = 0
    uniq_char_map = defaultdict(lambda: 0)
    max_l = 0
    while j < len(str):
        uniq_char_map[str[j]] = uniq_char_map[str[j]] + 1
        uniq_char_len = len(uniq_char_map)
        if uniq_char_len < k:
            j += 1
        elif uniq_char_len == k:
            print(uniq_char_map, i, j)
            max_l = max(max_l, j - i + 1)
            j += 1
        elif uniq_char_len > k:
            while uniq_char_len > k:
                uniq_char_map[str[i]] = uniq_char_map[str[i]] - 1
                if uniq_char_map[str[i]] == 0:
                    del (uniq_char_map[str[i]])
                    uniq_char_len -= 1
                i += 1

            j += 1
    return max_l


str = 'abcbdbdbbdcdabd'
# str = 'aabacbebebe'
print(longest_substr_of_k_distinct_char(str, 3))
