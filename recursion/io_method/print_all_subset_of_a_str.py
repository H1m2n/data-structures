# same solution nwe need to provide in case we are asking for print
# power set, subsequences

# Recommend ---> draw recursion tree yourself, the code is just a cakewalk
def solve(output, input):
    if len(input) == 0:
        # we are getting output at leaf node when we are getting in/p length 0, so here
        # only we need to print output
        print(output)
        return
    op1 = output
    op2 = output
    op2 += input[0]

    input = input[1:]
    solve(op1, input)
    solve(op2, input)


def print_all_subset_of_a_str(input):
    solve('', input)


print_all_subset_of_a_str("ab")
