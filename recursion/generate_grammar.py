# leetcode question
# based on observation skill + IBH

# Problem statement - we have given a intitial grammar, we need to generate grammar for some steps
# and need to answer a query by using generated grammar
# given N = 1, k = 1, generated grammar -> 0
# for each new step from one bit 2 bit will be generated like below example
# 0 -> 0 1
# 1 -> 1 0

# grammar -->
#          k=1  2   3   4   5   6   7   8
# N = 1     0
# N = 2     0   1
# N = 3     0   1   1   0
# N = 4     0   1   1   0   1   0   0   1


# Observations --->
# 1. for each N + 1, generate length of grammar for particular row(N+1) is - len(N) * 2
# 2. if partition N + 1 from mid, then we observer that the
#     first half of (N+1) == N
#            eg: 0 1 1 0 (first half of N=4) == 0 1 1 0 (N=3)
#     second half of(N+1) == !N (complement of N)
#            eg: 1 0 0 1 (second half of N=4) == 1 0 0 1 (complement of N=3)

def solve(N, K):
    # base condn given in question
    if N == 1 or K == 1:
        return 0

    mid = ((N - 1) ** 2) // 2
    if K <= mid:
        return solve(N - 1, K)
    else:
        return abs(1 - solve(N - 1, K - mid))


print(solve(4, 1))
print(solve(4, 2))
print(solve(4, 3))
print(solve(4, 4))
print(solve(4, 5))
print(solve(4, 6))
print(solve(4, 7))
print(solve(4, 8))
