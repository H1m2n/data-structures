e_stack = [1, 2, 3, 4, 5]


def do_delete(e_stack, i, middle_i):
    if len(e_stack) == 0:
        return
    if i == middle_i:
        e_stack.pop()
        return
        # hypothesis function -> will do deletion, we need to take care about the induction
    last_e = e_stack[-1]
    e_stack.pop()
    do_delete(e_stack, len(e_stack) - 1, middle_i)
    e_stack.append(last_e)
    # expected out - [1, 2, 3, 4] 5
    # expected out - [1, 2, 3] 4
    # hit the base condition so now function will start returning, so before returning, current state is
    # [1, 2] and the last element is 4


def delete_a_middle_element_from_stack(e_stack):
    middle_i = len(e_stack) // 2
    do_delete(e_stack, len(e_stack) - 1, middle_i)


delete_a_middle_element_from_stack(e_stack)
print(e_stack)
