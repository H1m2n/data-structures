import collections
from typing import List
from collections import deque
import copy


class SolutionBk:
    def cal_left_sum(self, nums, left_pointer):
        left_sum = 0
        while left_pointer >= 0:
            if nums[left_pointer] == 1:
                left_sum += 1
            else:
                break
            left_pointer -= 1
        return left_sum

    def cal_right_sum(self, nums, right_pointer):
        right_sum = 0
        while right_pointer <= len(nums) - 1:
            if nums[right_pointer] == 1:
                right_sum += 1
            else:
                break
            right_pointer += 1
        return right_sum

    def solve(self, nums, k, resultant_sum, count_arr):
        if k == len(nums) - 1:
            return resultant_sum
        max_sum = resultant_sum[0]
        left_sum = self.cal_left_sum(nums, k - 1)
        right_sum = self.cal_right_sum(nums, k + 1)
        total_sum = left_sum + right_sum
        if max_sum < total_sum:
            max_sum = total_sum
        resultant_sum[0] = max_sum
        self.solve(nums, k + 1, resultant_sum, count_arr)
        return resultant_sum

    def longestSubarray(self, nums: List[int]) -> int:
        count_arr = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == 1:
                if count_arr[-1] == 0:
                    count_arr.append(1)
                else:
                    count_arr[-1] = count_arr[-1] + 1
            else:
                count_arr.append(0)
        print(count_arr)
        out = self.solve(nums, 0, [0])
        return out[0]


class Solution:
    def get_left_ones(self, nums):
        dp_nums = copy.copy(nums)
        i, j = (0, 1)
        while j < len(dp_nums):
            if dp_nums[j] == 1:
                dp_nums[j] = 1 + dp_nums[i]
            i += 1
            j += 1
        return dp_nums

    def get_right_ones(self, nums):
        dp_nums = copy.copy(nums)
        i, j = (len(nums) - 1, len(nums) - 2)
        while j >= 0:
            if dp_nums[j] == 1:
                dp_nums[j] = 1 + dp_nums[i]
            i -= 1
            j -= 1
        return dp_nums

    def get_max_sum(self, nums, left_ones_list, right_ones_list):
        left_sum, right_sum = (nums[0], 0)
        max_sum = left_sum + right_sum
        for i in range(1, len(nums) - 1):
            left_sum = left_ones_list[i - 1]
            right_sum = right_ones_list[i + 1]
            total_sum = left_sum + right_sum
            if max_sum < total_sum:
                max_sum = total_sum
        return max_sum

    def longestSubarray(self, nums: List[int]) -> int:
        """
        Approach ->
        1. get the track of left ones count
        2. get the track of right ones count
        3. now for getting maximum, where at which position we are at in nums array(suppose ith position),
           lookup at (i-1)th index of left_ones_list and (i+1)th index of right_ones_list
        """
        left_ones_list = self.get_left_ones(nums)
        right_ones_list = self.get_right_ones(nums)
        return self.get_max_sum(nums, left_ones_list, right_ones_list)


obj = Solution()
nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
# nums = [1, 1, 1]
# nums = [0, 0, 0]
# nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
# nums = [1, 1, 0, 1]
# nums = [1, 1]
print(obj.longestSubarray(nums))

# [, 2, 1, 0, 1, 0]
