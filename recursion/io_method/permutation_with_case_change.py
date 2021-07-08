# i/p -> AB
# o/p -> ab aB Ab AB

# Recommend ---> draw recursion tree yourself, the code is just a cakewalk
def solve(output, input):
    if len(input) == 0:
        # here also we will get final output at the leaf node
        print(output)
        return

    # copying output of previous step as it is, because we need to take 2 decision that's why
    # in 2 variable we need to store next output after taking decision
    op1 = output
    op2 = output

    op1 += input[0].lower()  # store next input in lower form
    op2 += input[0].upper()  # store next input in upper form
    input = input[1:]  # smaller the input as, for 0th index character we already had taken a decision
    # recursive call for next set of i/p and o/p
    solve(op1, input)
    solve(op2, input)


def permutation_with_case_change(input):
    output = ''

    solve(output, input)


input = 'abc'
permutation_with_case_change(input)
