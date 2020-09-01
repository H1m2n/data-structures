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
