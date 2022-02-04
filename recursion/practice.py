s = ['h', 'e', 'l', 'l', 'o']


def reverse(s):
    if len(s) == 1:
        return s

    start_ele = s[0]
    tmp = reverse(s[1:])
    tmp.append(start_ele)
    return tmp


print(reverse(s))
