# Problem - we have give a number, that is denoting open and close bracket counts
# for eg n = 3, we have 3 open brackets and 3 closing brackets.
# We need to return all the possible balanced parenthesis

# balanced means
# (()) ✓, ()() ✓, ())( ✖

# Recommendation -> draw recursion tree for n = 3, for better understanding
# Note: This question require some observation skill

# Here, we have 2 choices, one for ( and another for ). But for closing bracket choices is not always available sometime
# because we need to make balanced parenthesis, while opening bracket choices is always available until we don't have it

# Observation for closing bracket choice ->
#    we can pick closing bracket only and only if - no of open brackets < no of closing brackets


def solve(open, close, out, arr):
    if open == 0 and close == 0:
        # print(out)
        arr.append(out)
        return

    if open != 0:
        # choices always availabe for open parenthesis until we don't have any
        op1 = out
        op1 += '('
        solve(open - 1, close, op1, arr)

    if open < close:
        op2 = out
        op2 += ')'
        solve(open, close - 1, op2, arr)


def generate_balanced_parenthesis(n):
    open = n
    close = n
    arr = []
    solve(open, close, '', arr)
    print(arr)


generate_balanced_parenthesis(3)
