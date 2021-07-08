# Problem: Josephus was in the army of jew. Once there was a war between roman army and jew army.
#          jew army was reside in cave and they are just 40 in strength and roman army size was big.
#          so they planned to kill themselves, so joseph has given them idea about killing.
#          He said, we will stand in circle and we count people from 1 to 7 (including itself) and will kill
#          7th person, so like wise we do this in repeatition and at last only one man will be alive, he should
#          suicide himself.

#          so we need to find out safe position(if we start position from 1 to 40, safe position will be 24)

def delete_particular_ele(i, arr):
    if len(arr) == 0:
        return
    if len(arr) - 1 == i:
        # we need to delete that element from array
        arr.pop()
        return
    last_e = arr[-1]
    arr.pop()
    delete_particular_ele(i, arr)
    arr.append(last_e)


arr = [1, 2, 3, 4, 5]
delete_particular_ele(1, arr)
print(arr)


def solve(start, n, k, arr):
    if n == 1:
        return arr[0]

    end = (start + k) % n
    # we need to delete end index element from array
    delete_particular_ele(end, arr)
    # start = end + 1
    return solve(end, n - 1, k, arr)


def josephus_problem(n, k):
    arr = []
    for i in range(n):
        arr.append(i + 1)
    k = k - 1  # because he will count himself, when counting for killing someone
    start = 0
    out = solve(start, n, k, arr)
    print(out)


josephus_problem(40, 7)
