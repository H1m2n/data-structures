# Problem: We need to find out longest repeating subsequqnces that should be repeating itself

s = "AABEBCDD"


# ans = "ABD" -> "ABD" is repeating 2 times

# Approach ->
# create another duplicate string
# so s1 = "AABEBCDD" and s2 = "AABEBCDD"

# we need to find out LCS by checking across indices(i and j), so i should not be equal to j
# why so?
# ans - A A
#       A A
# a character will be repeating if and only if it lies on another indices too
# as we can see in above exp t[0][0] == t[1][1] and t[0][1] == t[1][0]

def top_down_LCS(s1, s2, n, m):
    # matrix of (n + 1) * (m + 1)
    t = [[None for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1] and i != j:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    return t[i][j]


s1 = "AABEBCDD"
s2 = "AABEBCDD"
print(top_down_LCS(s1, s2, len(s1), len(s2)))
