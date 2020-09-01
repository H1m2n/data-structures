def bubble_sort(input, start_index=0, last_index=-1):
    if -len(input) == last_index:
        return
    for i, x in enumerate(input[start_index:last_index]):
        print("Before swapping - {}".format(input))
        print("{} - {}".format(i, i + 1))
        if x > input[i + 1]:
            tmp_elem = input[i + 1]
            input[i + 1] = input[i]
            input[i] = tmp_elem
        else:
            print("not executed")
        print("After swapping - {}".format(input))

    print('-------------------------------')

    last_index = last_index - 1
    bubble_sort(input, start_index, last_index)


# a = [1,2,3,4,5]
# a = [5, 4, 3, 2, 1]
a = [2, 5, 4, 3, 1]
bubble_sort(a)
print(a)
