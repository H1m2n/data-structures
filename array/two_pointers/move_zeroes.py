# https://leetcode.com/problems/move-zeroes/
def move_zeroes(nums):
    i, j = (0, 1)
    # [0,1,0,3,12]
    # [1,0,0,3,12]
    # [1,3,0,0,12]
    # [1,3,12,0,0]
    # compare value at i index if 0
    # if true then swap element and move i and
    while j < len(nums):
        if nums[i] != 0:
            i += 1
            j += 1
            continue
        # if we get nums[i] == 0
        #     now compare nums[j] with 0, if yes then swap i and j
        #                                 if no then increase j and loop continue until we don't get > 0 ele
        if nums[j] != 0:
            nums[i], nums[j] = (nums[j], nums[i])
            i += 1
            j += 1
        else:
            j += 1


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)
