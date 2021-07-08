# Problem: we have given an expression, we need to do partitions in such a way that expression will evaluate to True.
# so we need to find out the no of ways
# expression -> T | F & T ^ F

# xor table ->
#  T T -> F
#  F F -> F
#  T F -> T
#  F T -> T

# if i have 2 false and 4 True then no of ways to evaluate xor operations to True will be
# 2 * 4 = 8, so we need to pass one more variable here is_true, for one time getting no of ways to evaluate sub-expr
# to False and one time getting no of ways to evaluate sub-expr to True


def solve(expr, i, j, is_true):
    # base cond
    if i > j:
        return False
    if i == j:
        return is_true == expr[i]
    ans = 0
    k = i + 1
    while k <= j - 1:
        lt = solve(expr, i, k - 1, 'T')
        lf = solve(expr, i, k - 1, 'F')
        rt = solve(expr, k + 1, j, 'T')
        rf = solve(expr, k + 1, j, 'F')

        # we need to find no ways for all demand(True / False that we are demanding by is_true)
        if expr[k] == '&':
            # we need to find total no of ways, if we can evaluate an expression to False and True
            if is_true == 'F':
                ans += lt and rf + lf and rt + lf and rf
            else:
                ans += lt and rt

        elif expr[k] == '|':
            if is_true == 'F':
                ans += lf or rf
            else:
                ans += lt or rf + lf or rt + lt or rt
        else:
            if is_true == 'F':
                ans += lf ^ rf + lt ^ rt
            else:
                ans += lt ^ rf + lf ^ rt

        k += 2

    return ans


def evaluate_expression_to_true(expr):
    return solve(expr, 0, len(expr) - 1, 'T')


expr = "T | F & T ^ F"
print(evaluate_expression_to_true(expr))
