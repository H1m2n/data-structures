# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/submissions/

def min_operation_to_reduce_x_to_0(nums, x):
    # we need to find min value of k(operations)
    # for that we need to find longest subarray so that we meet this condition ->
    # (sum of k numbers == X), where k should be min
    # total sum - X = some value
    # so we need to find out longest subarray that have sum amount of (total sum - X)
    cond_sum = sum(nums) - x
    if cond_sum == 0:
        # that means we need to pick all element from array to reduce x
        return len(nums)
    i, j = (0, 0)
    max_len, total_sum = (0, 0)
    while j < len(nums):
        total_sum = total_sum + nums[j]
        if total_sum < cond_sum:
            j += 1
        elif total_sum == cond_sum:
            window_size = j - i + 1
            max_len = max(max_len, window_size)
            j += 1
        elif total_sum > cond_sum:
            # increment i until we fund total_sum <= cond_sum
            while total_sum > cond_sum and i < len(nums):
                total_sum = total_sum - nums[i]
                i += 1
            # print(total_sum)
            if total_sum == cond_sum:
                window_size = j - i + 1
                max_len = max(max_len, window_size)
            j += 1
    if max_len == 0:
        return -1
    k = len(nums) - max_len
    return k


nums = [1, 1, 4, 2, 3]
x = 5

nums = [3, 2, 20, 1, 1, 3]
x = 10

nums = [5, 6, 7, 8, 9]
x = 4

nums = [5, 2, 3, 1, 1]
x = 5

nums = [1, 1]
x = 3

nums = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
x = 134365
print(min_operation_to_reduce_x_to_0(nums, x))
