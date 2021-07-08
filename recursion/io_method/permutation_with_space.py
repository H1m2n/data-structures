# i/p -> 'ABC'
# o/p -> 'A_BC', 'AB_C', 'A_B_C', 'ABC'


# Recommend ---> draw recursion tree yourself, the code is just a cakewalk

def solve(output, input):
    if len(input) == 0:
        # here also o/p we will get at the leaf node
        print(output)
        return

    op1 = output
    op2 = output

    op1 += input[0]
    op2 += f'_{input[0]}'
    input = input[1:]
    solve(op1, input)
    solve(op2, input)


def permutation_with_space(input):
    output = input[0]
    input = input[1:]
    solve(output, input)


input = 'ABC'
permutation_with_space(input)
