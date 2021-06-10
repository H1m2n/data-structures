# https://leetcode.com/problems/permutation-in-string/

def permutation_in_string(s1, s2):
    char_dict = {}
    distinct_count = 0
    for x in s1:
        if x in char_dict:
            char_dict[x] = char_dict[x] + 1
        else:
            char_dict[x] = 1
            distinct_count += 1
    k = len(s1)

    i, j = (0, 0)
    while j < len(s2):
        if s2[j] in char_dict:
            char_dict[s2[j]] = char_dict[s2[j]] - 1
            print(char_dict)
            if char_dict[s2[j]] == 0:
                distinct_count -= 1

        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            if distinct_count == 0:
                return True
            if s2[i] in char_dict:
                char_dict[s2[i]] = char_dict[s2[i]] + 1
                if char_dict[s2[i]] == 1:
                    distinct_count += 1
            i += 1
            j += 1
    return False


# s1, s2 = ('ab', 'eidbaooo')
s1, s2 = ("ab", "eidboaoo")
s1 = "abcdxabcde"
s2 = "abcdeabcdx"
print(permutation_in_string(s1, s2))
# {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'x': 1, 'e': 1} 6
# {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1, 'x': 1} 6
