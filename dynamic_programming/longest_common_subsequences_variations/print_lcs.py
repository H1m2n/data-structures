s1 = "abcdghee"
s2 = "abdfhrxzye"


def print_lcs(s1, s2, n, m):
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

    # for printing LCS, we need to backtrack from matrix.
    # how we generate the matrix, logic is ---->
    # 1. we compare s[i-1] and s[j-1], if they are equal in t[i][j] block = 1 + t[i-1][j-1]
    # 2. if not equal then whatever the max is at t[i][j-1] and t[i-1][j], we wrote that value

    i, j = (n, m)
    ans = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if t[i][j - 1] > t[i - 1][j]:
                j -= 1
            else:
                i -= 1
    return ans[::-1]


print(print_lcs(s1, s2, len(s1), len(s2)))
