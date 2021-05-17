# This problem is related to previous longest_substr_of_k_distinct_char
# here the condition will be sum of all values of keys == no of keys
from collections import defaultdict


def longest_substr_with_no_repeating_char(str):
    i = j = 0
    max_l = 0
    uniq_char_map = defaultdict(lambda: 0)
    while j < len(str):
        uniq_char_map[str[j]] = uniq_char_map[str[j]] + 1
        candidate_cond = sum(list(uniq_char_map.values())) - len(uniq_char_map)
        # if candidate_cond == 0 then we get the candidate
        if candidate_cond == 0:
            max_l = max(max_l, len(uniq_char_map))
            print(uniq_char_map)
            j += 1
        elif candidate_cond > 0:
            while candidate_cond > 0:
                uniq_char_map[str[i]] = uniq_char_map[str[i]] - 1
                if uniq_char_map[str[i]] == 0:
                    del (uniq_char_map[str[i]])
                candidate_cond = sum(list(uniq_char_map.values())) - len(uniq_char_map)
                i += 1
            j += 1
    return max_l


str = 'pwabwabcde'
print(longest_substr_with_no_repeating_char(str))
