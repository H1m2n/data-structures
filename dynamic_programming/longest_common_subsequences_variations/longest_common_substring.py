# s1 = "abcdghee"
# s2 = "abdfhrxzye"

s1 = "aacabdkacaa"
s2 = s1[::-1]

# 0 1 2 3 4 5 6 7 8 9 10
# a a c a b d k a c a a
# a a c a k d b a c a a

# LCS = "abdhe"
# ans(longest_common_substring) = "ab"


def longest_common_substring(s1, s2, n, m):
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
                t[i][j] = 0

    longest_common_substr = 0
    for i in range(n + 1):
        for j in range(m + 1):
            longest_common_substr = max(longest_common_substr, t[i][j])
    print(t)
    return longest_common_substr


# longest_common_substring ---> we can't return t[i][j] because common substring can lie anywhere, so we need to return
# maximum by iterating on matrix
# [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ]

# longest_common_subsequence --->
# [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#     [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#     [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3],
#     [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3],
#     [0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4],
#     [0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 5],
#     [0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 5]
# ]


print(longest_common_substring(s1, s2, len(s1), len(s2)))
