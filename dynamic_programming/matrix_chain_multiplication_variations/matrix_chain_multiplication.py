# Problem: we have given an array, that will form matrices. so let say suppose we can form n numbber of matrix
# so we need to find out minimum cost(no of multiplications should be min) while we do multiplications of the matrix

# Note: for multiplying 2 matrix, below is the condition
#       mat1 = 5 * 10
#       mat2 = 10 * 20
#       no of columns of mat1 == no of rows of mat2, then only we can multiply a matrix
#       and the size of resultant matrix will be 5 * 20
#       multiplication cost = 5 * 10 * 20

# suppose we have given matrix A1, A2, A3, A4
# no of ways to multiply it -> ((A1 * A2) (A3 * A4))
#                           -> (A1 * (A2 * A3) * A4)
#                           -> (A1 * A2 * (A3 * A4)), so like we may have n no ways......


# for eg:  A = 10 * 30
#          B = 30 * 5
#          C = 5 * 60
# multiplication ways -> (A*(B*C)) -> cost (30 * 5 * 60) + (10 * 30 * 60) = 9000 + 18000 = 27000
#                     -> ((A*B)*C) -> cost (10 * 30 * 5) + (10 * 5 * 60) = 1500 + 3000 = 4500


# arr = [40, 20, 30, 10, 30]
# Below is the dimension of matrices for given array
# A1 = 40 * 20
# A2 = 20 * 30
# A3 = 30 * 10
# A4 = 10 * 30

# so the general formula for creating dimension is Ai = A[i-1] * A[i]


# Approach:
# 1. get the valid i and j index on array.
#    so i = 1 and j = len(arr) - 1, i couldn't be 0 because we need 2 element for forming matrix according to
#    formula(Ai = A[i-1] * A[i])
# 2. get the range of k, for moving it between i to j
#    k = 1..j-1, why j - 1? because at a point when we do partition of an array, then we should get valid atleast
#    at least a valid matrix
# 3. base condition -> i >= j, > is already invalid, but why i == j? because we can't make matrix for 1 element,
#    we need at-least 2 elements


def solve(arr, i, j):
    if i >= j:
        return 0

    min_cost = 10000000000  # arbitrary max no, that should be pick from constraint
    k = i
    while k <= j - 1:
        tmp_ans1 = solve(arr, i, k)
        tmp_ans2 = solve(arr, k + 1, j)
        tmp_ans = tmp_ans1 + tmp_ans2 + (arr[i - 1] * arr[k] * arr[j])
        if min_cost > tmp_ans:
            min_cost = tmp_ans
        k += 1
    return min_cost


dp = {}


def memoized_solve(arr, i, j):
    if i >= j:
        return 0

    min_cost = 10000000000  # arbitrary max no, that should be pick from constraint
    k = i
    while k <= j - 1:
        if (i, k) in dp:
            tmp_ans1 = dp[(i, k)]
        else:
            tmp_ans1 = memoized_solve(arr, i, k)
            dp[(i, k)] = tmp_ans1

        if (k + 1, j) in dp:
            tmp_ans2 = dp[(k + 1, j)]
        else:
            tmp_ans2 = memoized_solve(arr, k + 1, j)
            dp[(k + 1, j)] = tmp_ans2
        tmp_ans = tmp_ans1 + tmp_ans2 + (arr[i - 1] * arr[k] * arr[j])
        if min_cost > tmp_ans:
            min_cost = tmp_ans
        k += 1
    return min_cost


def matrix_chain_multiplication(arr):
    return memoized_solve(arr, 1, len(arr) - 1)
    # return solve(arr, 1, len(arr) - 1)


# (arr[i - 1] * arr[k] * arr[j]) - how we get this??
# [40, 20, 30, 10, 30]
# if suppose k is at the 1st occurrence of 30
# tmp_ans1 = 40 * 20 * 30 <---- This cost will be calculated by left partition -> now matrix dimension = 40 * 30
# tmp_ans2 = 30 * 10 * 30 <---- This cost will be calculated by right partition-> now matrix dimension = 30 * 30
# so now resultant matrix should be 40 * 30 * 30, so here we can use below formula to calculate cost of resultant matrix
# arr[i - 1] * arr[k] * arr[j], at last we need to sum-up all these cost to get the temp ans
arr = [40, 20, 30, 10, 30]
print(matrix_chain_multiplication(arr))
