def max_product(nums, n):
    nums.sort(reverse=True)
    return nums[0] * nums[1] * nums[2]


nums = [1, 2, 3, 4]
nums = [-1,-2,-3,-4]
print(max_product(nums, 4))
