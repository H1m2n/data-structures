def find_index(sorted_nums, num):
    # binary search
    i, j = (0, len(sorted_nums) - 1)
    while i <= j:
        # print(i, j)
        middle_i = (i + j) // 2
        if num == sorted_nums[middle_i]:
            return middle_i
        elif num < sorted_nums[middle_i]:
            j = middle_i - 1
        elif num > sorted_nums[middle_i]:
            i = middle_i + 1
    # print(i, j)

# 10
# 7
# [5, 4, 1, 2, 10, 3, 6, 8, 9]

sorted_nums = [1, 2, 3, 4, 5]
sorted_nums = [1, 3, 10, 12]
num = 7
print(find_index(sorted_nums, num))


# [1, 3, 5, 6]




