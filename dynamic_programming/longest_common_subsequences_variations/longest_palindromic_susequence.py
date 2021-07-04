# Problem: We have given a string we need to find out longest plaidromic subsequence

a = "agbcba"

# How it is similar to LCS?
# ans: we are talking about here subsequence and in o/p we need to return integer

# if a string is palindrome that means if we reverse a string then inside that string the subsequences order
# should follow the rule of palindrome property

# so reverse of a will be -> "abcbga"

# now to answer the problem we just need to find out LCS

# LPS(a) = LCS(a, reverse(a))
