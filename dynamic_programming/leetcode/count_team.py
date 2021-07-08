steps = 0


def generate_inc_seq(out, i, input_len, arr, out_arr):
    global steps
    steps += 1
    if i == input_len:
        print(out)
        if len(out) == 3:
            print(out)
            out_arr.append(out)
        return

    op1 = out
    if int(op1[-1]) < arr[i] and len(op1) < 3:
        # choice to include, only available if last element in o/p is less than arr[i]
        op1 += str(arr[i])
        generate_inc_seq(op1, i + 1, input_len, arr, out_arr)

    # choice to not include is always available
    op2 = out
    generate_inc_seq(op2, i + 1, input_len, arr, out_arr)


def generate_dec_seq(out, i, input_len, arr, out_arr):
    global steps
    steps += 1
    if i == input_len:
        if len(out) == 3:
            out_arr.append(out)
        return

    op1 = out
    if int(op1[-1]) > arr[i] and len(op1) < 3:
        # choice to include only available if last element in o/p is greater than arr[i]
        op1 += str(arr[i])
        generate_dec_seq(op1, i + 1, input_len, arr, out_arr)

    # choice to not include is always available
    op2 = out
    generate_dec_seq(op2, i + 1, input_len, arr, out_arr)


def count_team(arr):
    out_arr = []
    dp = {}
    n = len(arr)
    generate_inc_seq('2', 0 + 1, len(arr), arr, out_arr)
    # for i, x in enumerate(arr):
    #     generate_inc_seq(str(x), i + 1, len(arr), arr, out_arr)
    #     generate_dec_seq(str(x), i + 1, n, arr, out_arr)
    return len(out_arr)


count_team([2, 5, 3, 4, 1])

# count_team([2, 1, 3])
#
# count_team([1, 2, 3, 4])

# print(count_team([x for x in range(1, 200)]))
print('**********')
print(steps)
