num = 12321
orig_num = num

''
# 1
# 2
# 3
# newnum = 10 * 1 + rem
#
# 12
# newnum = newnum * 10 + rem
# newnum = 1
# 1 * 10 + 2


# i = 0
# l = []
# while (num != 0):
#     rem = num % 10
#     num = num // 10
#     l.append(str(rem))
# # print(l)
#
#
# print(int(''.join(l)) == orig_num)


def palindrome_check(num):
    i = 0
    newnum = 0
    while (num != 0):
        rem = num % 10
        num = num // 10
        newnum = newnum * 10 + rem
        i += 1
    return newnum == orig_num


# print(l)


# print(int(''.join(l)) == orig_num)

print(palindrome_check(num))
