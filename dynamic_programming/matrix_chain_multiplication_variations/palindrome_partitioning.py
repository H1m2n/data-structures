# Problem: we need to find out min no of partitions so that the resultant partition will be palindrome

# eg: nitik
# here we need 2 partitions
# p1 = n, p2 = iti, p3 = k

def is_palindrome(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def solve(s, i, j):
    # 1. identify base cond
    if i > j:
        return 0
    # here, there will be one more base condition, if a partition is already a palindrome, than we
    # don't need to do further partitioning
    if is_palindrome(s, i, j):
        return 0

    # 2. identify i and j, so i = 0, j = len(s) - 1
    # 3. identify movement of k, k can move from i to j
    #    range of k will be i..j-1, why j-1? because if we place k at j, then we can't do further 2 partitioning
    ans = 10000000  # arbitrary number
    k = i
    while k <= j - 1:
        tmp_ans1 = solve(s, i, k)
        tmp_ans2 = solve(s, k + 1, j)
        tmp_ans = tmp_ans1 + tmp_ans2 + 1
        if ans > tmp_ans:
            ans = tmp_ans
        k += 1
    return ans


def palindrome_partitioning(s):
    return solve(s, 0, len(s) - 1)


s = 'nitik'
print(palindrome_partitioning(s))
