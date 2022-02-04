from typing import List
import copy


class SolutionBk:
    def cal_alt_sum(self, arr):
        even_sum, odd_sum = (0, 0)
        for i in range(len(arr)):
            if i % 2 == 0:
                even_sum += arr[i]
            else:
                odd_sum += arr[i]
        return even_sum - odd_sum

    def solve(self, nums, out, out_arr, start, dp):
        if start == len(nums):
            out_arr.append(self.cal_alt_sum(out))
            return out

        op1 = copy.copy(out)
        op1.append(nums[start])

        self.solve(nums, op1, out_arr, start + 1, dp)

        op2 = copy.copy(out)
        self.solve(nums, op2, out_arr, start + 1, dp)

    def maxAlternatingSum(self, nums: List[int]) -> int:
        out_arr = []
        dp = {}
        self.solve(nums, [], out_arr, 0, dp)
        return max(out_arr)


class Solution:
    # intuition is: our index pattern is like -> even, odd, even, odd
    # as we need to sum up of even index element so at start is_pos flag should be True
    # if we making a choice to select, then we need to set is_pos to False(because now next coming element will be at odd index).
    # if we making a choice to not select, then is_pos flag should be same that we have passed in argument
    def solve(self, nums, i, is_pos, dp):
        if i == len(nums):
            return 0
        if (i, is_pos) in dp:
            return dp[(i, is_pos)]
        curr_value = nums[i] if is_pos else -nums[i]
        dp[(i, is_pos)] = max(curr_value + self.solve(nums, i + 1, not is_pos, dp), self.solve(nums, i + 1, is_pos, dp))
        return dp[(i, is_pos)]

    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        out = self.solve(nums, 0, True, dp)
        return out


obj = Solution()
# nums = [6, 2, 1, 2, 4, 5]
# nums = [5, 6, 7, 8]
nums = [4, 2, 5, 3]
print(obj.maxAlternatingSum(nums))
