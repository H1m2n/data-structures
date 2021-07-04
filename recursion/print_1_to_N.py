arr = []


def print_num(n):
    # base cond -> smallest valid i/p or largest invalid i/p, from where recursion should break
    if n == 0:
        return 0

    print_num(n - 1)  # <-- hypothesis step will give result for sample(6), o/p -> 1, 2, 3, 4, 5, 6
    arr.append(
        n)  # <--- induction step after calling function again for n-1 (7-1=6), we need to save the current no ie: 7


n = 7
print_num(n)
print(arr)

reverse_arr = []


def print_reverse(n):
    if n == 0:
        return 0

    reverse_arr.append(n)
    print_reverse(n - 1)


n = 7
print_reverse(n)
print(reverse_arr)
