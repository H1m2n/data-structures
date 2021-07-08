# Problem: We need to print N binary numbers having more ones or equals than zeroes
# for eg: N = 5

# Recommendation -> draw recursion tree for n = 3, for better understanding
# Note: This question require some observation skill

# Observations ->
#    1. at 1st position we can't keep 0 at place, because when suppose we are at first index,
#       so for that index prefix will be just 0. so in this case no of zeros(1) > no of ones(0), that violate the condn
#    2. we have always available choices for ones, but for zeroes we have choices available only and only if
#       no of ones > no of zeroes
#


def solve(ones, zeroes, n, out, arr):
    if n == 0:
        print(out)
        arr.append(out)
        return

    op1 = out
    op1 += '1'
    solve(ones + 1, zeroes, n - 1, op1, arr)
    if ones > zeroes:
        # for zeroes we have choices available only and only if no of ones > no of zeroes
        op2 = out
        op2 += '0'
        solve(ones, zeroes + 1, n - 1, op2, arr)


def print_binary_no(n):
    ones = 0
    zeroes = 0
    arr = []
    out = '1'
    solve(ones + 1, zeroes, n - 1, out, arr)
    print(arr)


print_binary_no(3)
