# [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# [-12, -6, -13, -5, 6, -7, 5, -3, 11]
# [-12, -6, -13, -5, -3, -7, 5, 6, 11]

#
# [-12, 11]  [-13, -5]  [6, -7] [5, -3] [-6] --> [-12, 11]  [-13, -5]  [-7, 6] [-3, 5] [-6]
#
# [-12, 11, -13, -5], [-7, 6, -3, 5], [-6] ----> [-12, -13, -5, 11] [-7, -3, 6, 5] [-6]
#
# [-12, -13, -5, 11, -7, -3, 6, 5] [-6] -------> [-12, -13, -5, -7, -3, 11, 6, 5] [-6]
#
# [-12, -13, -5, -7, -3, 11, 6, 5, -6]  --------> [-12, -13, -5, -7, -3, -6, 11, 6, 5]


def move_neg_and_pos_numbers(part_arr):
    exit_flag = False
    j = len(part_arr) - 1
    for i, x in enumerate(part_arr):
        # then move this element at the end of arr, while moving at index get first negative number from last
        if x > 0:
            while not (part_arr[j] < 0):
                if j == i:
                    # This is the saturation point
                    exit_flag = True
                    break
                j -= 1

            part_arr[j], part_arr[i] = (part_arr[i], part_arr[j])
        if exit_flag:
            break


# worst case complexity: O(n^2) for all positive number
# average case complexity: O(n*k)

#
# arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# move_neg_and_pos_numbers(arr)
# print(arr)
#
# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# move_neg_and_pos_numbers(arr)
# print(arr)
#
# arr = [-1, -2, -3, -4]
# move_neg_and_pos_numbers(arr)
# print(arr)
#
# arr = [1, -1, -2, -3]
# move_neg_and_pos_numbers(arr)
# print(arr)
#
# arr = [1, 2, 3, 4]
# move_neg_and_pos_numbers(arr)
# print(arr)


def move_numbers(arr):
    left_count = 0
    right_count = len(arr) - 1
    while left_count <= right_count:
        if arr[left_count] > 0 > arr[right_count]:
            arr[right_count], arr[left_count] = (arr[left_count], arr[right_count])
            right_count -= 1
            left_count += 1
        elif arr[left_count] > 0 and arr[right_count] > 0:
            right_count -= 1
        elif arr[left_count] < 0 and arr[right_count] < 0:
            left_count += 1
        else:
            left_count += 1
            right_count -= 1
        # print((left_count, right_count))


#  time complexity //O(n)
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
move_numbers(arr)
print(arr)

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
move_numbers(arr)
print(arr)

arr = [-1, -2, -3, -4]
move_numbers(arr)
print(arr)

arr = [1, -1, -2, -3]
move_numbers(arr)
print(arr)

arr = [1, 2, 3, 4]
move_numbers(arr)
print(arr)
