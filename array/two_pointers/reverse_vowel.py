# https://leetcode.com/problems/reverse-vowels-of-a-string/
# "hello"
def reverse_vowel(s):
    i, j = (0, len(s) - 1)
    vowels = ['a', 'e', 'i', 'o', 'u']
    arr_str = list(s)
    while i <= j:
        if arr_str[i].lower() in vowels and arr_str[j].lower() in vowels:
            # do swap
            arr_str[i], arr_str[j] = (arr_str[j], arr_str[i])
            i += 1
            j -= 1
        elif arr_str[i].lower() in vowels and arr_str[j].lower() not in vowels:
            j -= 1
        elif arr_str[i].lower() not in vowels and arr_str[j].lower() in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(arr_str)


s = 'hello'
s = "leetcode"
print(reverse_vowel(s))
