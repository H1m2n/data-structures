def reversing_approach(nums, k):
    def reverse(start_i, end_i, nums):
        while start_i <= end_i:
            nums[start_i], nums[end_i] = (nums[end_i], nums[start_i])
            start_i += 1
            end_i -= 1

    n = len(nums)
    k = k % n  # to ensure if k > n, k should lie in between range of 1 to n
    reverse(0, n - k - 1, nums)
    reverse(n - k, n - 1, nums)
    reverse(0, n - 1, nums)


def rotate_arr_k_times(nums, k):
    # Time complexity O(n)
    # Space Complexity O(n)

    e_stack = []
    i = len(nums) - 1
    while i >= 0:
        e_stack.append(nums[i])
        i -= 1

    i = 0
    while len(e_stack) > 0:
        final_i = (i + k) % len(nums)
        nums[final_i] = e_stack[-1]
        e_stack.pop()
        i += 1


nums = [1, 2, 3, 4, 5]
k = 3
# rotate_arr_k_times(nums, k)
reversing_approach(nums, k)
