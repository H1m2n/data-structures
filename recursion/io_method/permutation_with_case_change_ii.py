# Problem: we have given a string, we need to change the case, and need to print all possible permiutation
# but the twist is here we also have digits in string

# Recommend ---> draw recursion tree yourself, the code is just a cakewalk
def solve(output, input):
    if len(input) == 0:
        print(output)
        return

    op1 = output
    op2 = output

    char = input[0]
    input = input[1:]
    if not char.isalpha():
        op1 += char
        solve(op1, input)
    else:
        op1 += char.lower()
        op2 += char.upper()
        solve(op1, input)
        solve(op2, input)


def permutation_with_case_change_ii(input):
    solve('', input)


input = 'a1B2'
permutation_with_case_change_ii(input)
