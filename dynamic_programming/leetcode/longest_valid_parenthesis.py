# https://leetcode.com/problems/longest-valid-parentheses/

# Approach ->
# 1. we need to get the count of opening braces into an array,
# 2. whenever we encounter a closing bracket, we need to convert a one to zero, from backside,
# 3. at last for the ans, we need to calculate max consecutive zero from resultant array.
# so ans will be 2 * (max consecutive zero)

def generate_binary_list(s):
    arr = []
    for x in s:
        if x == '(':
            arr.append(1)
        else:
            j = len(arr) - 1
            while j >= 0 and arr[j] != 1:
                j -= 1
            if j < 0:
                arr.append(2)
            else:
                arr[j] = 0
    return arr


def cal_max_consecutive_ones(arr):
    max_cons, count = (0, 0)
    for x in arr:
        if x == 0:
            count += 1
            max_cons = max(max_cons, count)
        else:
            count = 0
    return 2 * max_cons


def longest_valid_parenthesis(s):
    arr = generate_binary_list(s)
    print(arr)
    return cal_max_consecutive_ones(arr)


s = '((()())()(((()())()()'
s = "(()"
s = ")()())"
s = ""
s = ")()())()()("
print(longest_valid_parenthesis(s))
