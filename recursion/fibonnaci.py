def stair_up(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return stair_up(n - 1) + stair_up(n - 2) + stair_up(n - 3)


print(stair_up(4))


def perm(s, i, out):
    if i == len(s) - 1:
        out.append(s)
        print(s)
        return
    for idx in range(len(s)):
        if idx < i:
            continue
        s[i], s[idx] = (s[idx], s[i])
        perm(s, i + 1, out)
        s[i], s[idx] = (s[idx], s[i])


out = []
perm(['a', 'b', 'c'], 0, out)
print(out)

# for idx in range(len(['a', 'b', 'c'])):
#     print(idx)
print('********************************')


def arr_test(arr, i, val):
    if i == len(arr) - 1:
        return arr[i]
    ret_val = arr_test(arr, i + 1, arr[i + 1])
    print(ret_val)
    return val


arr_test([1, 2, 3, 4], -1, None)

print('***************')


def print_arr(arr, i, val):
    if i == len(arr) - 1:
        return arr[i]
    sum_until_now = print_arr(arr, i + 1, arr[i + 1])
    curr_sum = val + sum_until_now
    return curr_sum


print(print_arr([1, 2, 3, 4], 0, 1))
