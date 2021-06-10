# https://leetcode.com/problems/max-consecutive-ones-iii/

def max_consecutive_ones(nums, k):
    # [1,1,1,0,0,0,1,1,1,1,0]
    # we will have a count variable there we store max number of flip of 0 to 1
    # loop through i to j and get count until we don't have count == 0
    # do calculation
    # if we get count == 0 do calculation.
    # for calculation get the max
    i, j = (0, 0)
    count = k
    max_ones, ones_count = (0, 0)
    while j < len(nums):
        ones_count += 1
        if nums[j] == 0:
            count -= 1

        if count >= 0:
            max_ones = max(max_ones, ones_count)
        elif count < 0:
            # increment i and decrement ones_count by one
            # if we encounter 0 at any position then increase count
            while count < 0:
                ones_count -= 1
                if nums[i] == 0:
                    count += 1
                i += 1
        j += 1
    return max_ones


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

# nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k = 3
#
# nums = [0, 0, 0, 1]
# k = 3

print(max_consecutive_ones(nums, k))
