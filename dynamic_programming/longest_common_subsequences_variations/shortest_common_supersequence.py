# Problem: We have given 2 string a and b, we need to find out shortest common supersequence

a = "geek"
b = "eke"

# one possible sequence is -> geek + eke = geekeke
# but this is the longest sequence where we will ave both the string

# we can make it shorter by leveraging LCS, things that are common we should write only once
# so from a + b remove LCS
# so answer will be -> len(a) + len(b) - LCS
