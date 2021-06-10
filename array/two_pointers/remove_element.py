# https://leetcode.com/problems/remove-element/

# [3,2,2,3]
# [2, 3, 2, 3]
# []
def remove_element(nums, val):
    i, j, num_len = (0, 1, 0)
    while j < len(nums):
        if nums[i] != val:
            i += 1
            j += 1
            continue

        if nums[j] != val:
            nums[i], nums[j] = (nums[j], nums[i])
            i += 1
            j += 1
        else:
            j += 1

    for x in nums:
        if x != val:
            num_len += 1
    return num_len


# nums = [3,2,2,3]
# val = 3
# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
# nums = [1]
# val = 1
# nums = [3,3]
# val = 3
# nums = [2]
# val = 3
nums = [3, 3]
val = 5

print(remove_element(nums, val))
print(nums)
