# Problem statement: we have given an array, we need to find target sum by assigning + or - sign to array elements
# such that the difference between 2 subsets will be equals to the target sum
# we need too find the no of counts


# This problem is exactly same as count_no_of_subset_with_given_diff.

# How?

# arr = [1, 1, 2, 3]
# target_sum = 1

# [+1, -1, -2, + 3] -> [1, 3] - [1, 2] = 1
# [-1, +1, -2, + 3] -> [1, 3] - [1, 2] = 1
# [+1, +1, +2, -3]  -> [1, 1, 2] - [3] = 1
# so answer will be 3
