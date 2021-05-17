from collections import defaultdict


# all permutation of a pattern is called anagram
def count_anagram1(str, pattern):
    # create a map and have count of each alphabet
    anagram_count = 0
    k = len(pattern)
    pattern_dict = {}
    distinct_char_count = 0
    for x in pattern:
        if x not in pattern_dict:
            pattern_dict[x] = 1
            distinct_char_count += 1
        else:
            pattern_dict[x] = pattern_dict[x] + 1
    print(pattern_dict)

    # while traversing we need to decrement the count in map
    # when we hit the window size check if distinct_char_count == 0
    # if 0 then we got one pattern
    i = j = 0
    break_var = 0
    while j < len(str):
        if pattern_dict.get(str[j]):
            pattern_dict[str[j]] = pattern_dict[str[j]] - 1
            if pattern_dict[str[j]] == 0:
                distinct_char_count -= 1
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            break_var += 1
            if break_var == 2:
                print(pattern_dict, distinct_char_count, i, j)
                break
            if distinct_char_count == 0:
                anagram_count += 1

            # before incrementing i we need to again put that char in dictionary and increment the count
            # as we have to do calculation again for the next window
            if str[i] in pattern_dict:
                pattern_dict[str[i]] = pattern_dict[str[i]] + 1
                distinct_char_count += 1
            i += 1
            j += 1

            # We don't need to include str[j] in dictionary as anyway at start of the loop we are decreasing count
            # when we get something available in dictionary so we don't required it due to unnecessary work

    return anagram_count


# all permutation of a pattern is called anagram
def count_anagram(str, pattern):
    # create a map and have count of each alphabet
    anagram_count = 0
    k = len(pattern)
    pattern_dict = {}
    distinct_char_count = 0
    for x in pattern:
        if x not in pattern_dict:
            pattern_dict[x] = 1
            distinct_char_count += 1
        else:
            pattern_dict[x] = pattern_dict[x] + 1
    print(pattern_dict)

    # while traversing we need to decrement the count in map
    # when we hit the window size check if distinct_char_count == 0
    # if 0 then we got one pattern
    i = j = 0
    window_dict = defaultdict(lambda: 0)
    while j < len(str):
        window_dict[str[j]] = window_dict[str[j]] + 1
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            print(window_dict)
            # check if window_dict is exactly same as pattern dict if its same then we found anagram substring
            window_dict[str[i]] = window_dict[str[i]] - 1
            if window_dict[str[i]] == 0:
                del (window_dict[str[i]])

            i += 1
            j += 1

    return anagram_count


str = 'aababaa'
pattern = 'aba'
# str = 'abbacdadcdab'
# pattern = 'abbc'
# out = 2
# bab a
# {'a': 1, 'b': 0} 1 2 4
print(count_anagram(str, pattern))
