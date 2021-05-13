# Q1: get the fibonaci number of a particular index

# fib series - 0, 1, 1, 2, 3, 5, 8, 13, 21
def fib_at_index(index):
    first_num, seco_num = (0, 1)
    output, count = (None, 0)
    while True:
        if count == index - 1:
            break
        next_num = first_num + seco_num
        first_num = seco_num
        seco_num = next_num
        output = next_num
        count += 1

    return output


def recc_feb_at_index(index):
    if index < 2:
        return index
    return recc_feb_at_index(index - 1) + recc_feb_at_index(index - 2)


def reverse_str_by_recc(str, start_index=0, end_index=-1):
    if len(str) // 2 == start_index:
        return str

    list_of_char = []
    list_of_char[:0] = str
    elem_at_last = list_of_char[end_index]
    elem_at_first = list_of_char[start_index]
    list_of_char[end_index] = elem_at_first
    list_of_char[start_index] = elem_at_last
    str = ''.join(list_of_char)
    start_index += 1
    end_index -= 1
    return reverse_str_by_recc(str, start_index, end_index)


print(reverse_str_by_recc('HimanshuYadav'))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def reverse(str, number_of_iteration, last_ele_i, first_ele_i=0):
    """
    Himanshu Yadav
    0...len(str)-1
    swap element

    1...

    :param str:
    :return:
    """
    if number_of_iteration == 0:
        return
    # first_ele_i = 0
    # last_ele_i = len(str) - 1
    str[first_ele_i], str[last_ele_i] = (str[last_ele_i], str[first_ele_i])
    number_of_iteration -= 1
    first_ele_i += 1
    last_ele_i -= 1
    reverse(str, number_of_iteration, last_ele_i, first_ele_i)


s = "Himanshu Yadav"
s = list(s)
reverse(s, len(s) // 2, len(s) - 1)

print("hi" + ''.join(s))


def fibonacci(n, acc, first=0, second=1):
    """
    n = 8
    0, 1, 1, 2, 3, 5, 8, 13
    :param n:
    :return:
    """
    if n == 2:
        return second
    number = first + second
    acc.append(number)
    first = second
    second = number
    return fibonacci(n - 1, acc, first, second)


arr = [0, 1]
print(fibonacci(8, arr))
print(arr)

print(factorial(5))
"""
5 * 4 * 3 * 2 * 1
factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)



5 * 24
"""
