# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# [0,0,1,1,1,2,2,3,3,4,5,6]
# we are just worried about the length no matter what it remains in array
def remove_duplicates_from_sorted_array(nums):
    i, j = (0, 1)
    num_len = 1
    while j < len(nums):
        num_len += 1
        if nums[i] == nums[j]:
            num_len -= 1
            nums.pop(j)
        else:
            i = j
            j += 1
    return num_len


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1, 2]
print(remove_duplicates_from_sorted_array(nums))
print(nums)