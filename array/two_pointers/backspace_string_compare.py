# https://leetcode.com/problems/backspace-string-compare/
# s = "ab#c", t = "acd#"
# "ab##", t = "c#d#"
def backspace_string_compare(s, t):
    s_stack = []
    for x in s:
        if x != '#':
            s_stack.append(x)
        else:
            if s_stack:
                s_stack.pop()

    t_stack = []
    for x in t:
        if x != '#':
            t_stack.append(x)
        else:
            if t_stack:
                t_stack.pop()
    return ''.join(s_stack) == ''.join(t_stack)


# s = "ab#c"
# t = "ad#c"
s = "ab##"
t = "c#d#"
print(backspace_string_compare(s, t))
