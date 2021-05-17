"""
Level - Hard
Problem:
We have one long string and one smaller string.
Smaller strings character should be present in longer string.
Condition is if a character count in smaller string is 2 then that character count in window should be >= 2

eg: s1 = "time to practice"
    s2 = "toc"
    out = "to prac"
"""
from collections import defaultdict


def min_window_substr(str, ptr):
    """
    pattern_map = {
        t: 1
        o: 1
        c: 1
    }
    :param str:
    :param ptr:
    :return:
    """
    pattern_map = defaultdict(lambda: 0)
    for x in ptr:
        pattern_map[x] = pattern_map[x] + 1
    distinct_char_count = len(pattern_map)

    i = j = 0
    min_l = 0
    cond_meet_in_loop = False
    while j < len(str):
        if str[j] in pattern_map:
            pattern_map[str[j]] = pattern_map[str[j]] - 1
            if pattern_map[str[j]] == 0:
                distinct_char_count -= 1

        if distinct_char_count > 0:
            j += 1
        elif distinct_char_count == 0:
            if cond_meet_in_loop:
                start_i, end_i = (i - 1, j - 1)
            else:
                start_i, end_i = (i, j)
            no_of_char_in_substr = end_i - start_i + 1
            print(i-1, j-1)
            print(f"no_of_char_in_substr - {no_of_char_in_substr}, start_i - {start_i}, end_i - {end_i}")
            if min_l == 0:
                min_l = no_of_char_in_substr
            else:
                min_l = min(min_l, no_of_char_in_substr)
            while distinct_char_count == 0:
                if str[i] in pattern_map:
                    pattern_map[str[i]] = pattern_map[str[i]] + 1
                    if pattern_map[str[i]] == 1:
                        distinct_char_count += 1
                        cond_meet_in_loop = True
                i += 1
            j += 1
    return min_l


s1 = "timetopractice"
s2 = "toc"
print(min_window_substr(s1, s2))
