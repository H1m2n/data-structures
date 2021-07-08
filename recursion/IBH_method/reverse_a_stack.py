e_stack = [1, 2, 3, 4, 5]


def insert_at_first(reversed_stack, ele):
    if len(reversed_stack) == 0:
        reversed_stack.append(ele)
        return
    last_e = reversed_stack[-1]
    reversed_stack.pop()
    insert_at_first(reversed_stack, ele)
    reversed_stack.append(last_e)


e_stack1 = [3, 2, 1]
ele = 10
insert_at_first(e_stack1, ele)
print(e_stack1)


def do_reverse(e_stack):
    if len(e_stack) == 1:
        return
        # hypothesis step:
    # function that we will written will give us o/p in this form
    # [4, 3, 2, 1], we need to take care to put 5 at its correct position
    # [3, 2, 1], we need to take care to put 4 at its correct position
    last_e = e_stack[-1]
    e_stack.pop()
    do_reverse(e_stack)
    insert_at_first(e_stack, last_e)


# o/p - > [5, 4, 3, 2, 1]
def reverse_a_stack(e_stack):
    do_reverse(e_stack)


reverse_a_stack(e_stack)
print(e_stack)
