"""
https://leetcode.com/problems/maximum-ascending-subarray-sum/
Problem: Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
"""


def maximum_ascending_sub_array_sum(nums):
    j = 1
    max_sum = e_sum = nums[0]
    while j < len(nums):
        if nums[j - 1] < nums[j]:
            e_sum = e_sum + nums[j]
        else:
            e_sum = nums[j]

        max_sum = max(max_sum, e_sum)
        j += 1
    return max_sum


print(maximum_ascending_sub_array_sum([100, 10, 1]))
