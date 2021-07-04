# problem statement: We have given 2 strings, we need to find out the longest common subsequence

s1 = "abcdghee"
s2 = "abdfhrxzye"

LCS = "abdhe"


# s1 = "abcdghee"
# s2 = "abdfhrxzyeqe"
# LCS = "abdhee"


# Approach ->
# we will always compare last elements of both the strings
# now it might be possible that last elements can be equal or not equal

# if last element is equal then we add 1 in answer and call LCS function again by dropping last elements of both
# the strings
# so the statement will be -> 1 + LCS(s1, s2, n-1, m-1), n = len(s1) and m = len(s2)

# if last elements are not equal, then here we will have 2 choices
#   1> take full chars of s1 and drop last element of s2
#   2> take full chars of s2 and drop last element of s1
#   now from both 1> and 2> get the max out of it from the choices


# recursive approach
def LCS(s1, s2, n, m):
    """
    s1: string 1
    s2: string 2
    n: len(s1)
    m: len(s2)
    """
    # base condition (Think of the smallest valid input)
    if n == 0 or m == 0:
        # if any of the string is empty then nothing will be common, so return 0
        return 0

    if s1[n - 1] == s2[m - 1]:
        return 1 + LCS(s1, s2, n - 1, m - 1)
    else:
        return max(LCS(s1, s2, n, m - 1), LCS(s1, s2, n - 1, m))


# memoized_map = {}
#
#
# # Memoized approach
# def memoized_LCS(s1, s2, n, m):
#     """
#     s1: string 1
#     s2: string 2
#     n: len(s1)
#     m: len(s2)
#     """
#     # base condition (Think of the smallest valid input)
#     if n == 0 or m == 0:
#         # if any of the string is empty then nothing will be common, so return 0
#         return 0
#
#     if (n, m) in memoized_map:
#         print('here...')
#         return memoized_map[(n, m)]
#     # print(memoized_map)
#     if s1[n - 1] == s2[m - 1]:
#         memoized_map[(n, m)] = 1 + memoized_LCS(s1, s2, n - 1, m - 1)
#         return memoized_map[(n, m)]
#     else:
#         memoized_map[(n, m)] = max(memoized_LCS(s1, s2, n, m - 1), memoized_LCS(s1, s2, n - 1, m))
#         return memoized_map[(n, m)]


# Memoized approach
def memoized_LCS():
    """
    s1: string 1
    s2: string 2
    n: len(s1)
    m: len(s2)
    """
    memoized_map = {}

    def LCS_cal(s1, s2, n, m):

        # base condition (Think of the smallest valid input)
        if n == 0 or m == 0:
            # if any of the string is empty then nothing will be common, so return 0
            return 0

        if (n, m) in memoized_map:
            # print('here...')
            return memoized_map[(n, m)]
        # print(memoized_map)
        if s1[n - 1] == s2[m - 1]:
            memoized_map[(n, m)] = 1 + LCS_cal(s1, s2, n - 1, m - 1)
            return memoized_map[(n, m)]
        else:
            memoized_map[(n, m)] = max(LCS_cal(s1, s2, n, m - 1), LCS_cal(s1, s2, n - 1, m))
            return memoized_map[(n, m)]

    return LCS_cal


def top_down_LCS(s1, s2, n, m):
    # matrix of (n + 1) * (m + 1)
    t = [[None for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])

    print(t)
    return t[i][j]


s1 = "aacabdkacaa"
s2 = s1[::-1]

print(LCS(s1, s2, len(s1), len(s2)))
# print(memoized_LCS(s1, s2, len(s1), len(s2)))
memoized_fun = memoized_LCS()
print(memoized_fun(s1, s2, len(s1), len(s2)))

print(top_down_LCS(s1, s2, len(s1), len(s2)))
