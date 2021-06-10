def max_no_of_vowels_in_k_segment(s, k):
    i, j = (0, 0)
    max_vowels, vowel_count = (0, 0)
    while j < len(s):
        if s[j] in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            max_vowels = max(max_vowels, vowel_count)
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel_count -= 1
            i += 1
            j += 1
    return max_vowels


s = "abciiidef"
k = 3
print(max_no_of_vowels_in_k_segment(s, k))
