from typing import List


class Solution:
    def memoized_cal(self, nums, i, j):
        if i >= j:
            return 0

        max_sum = 0
        k = i
        k_max = j - 1
        while k <= k_max:
            temp_ans1 = self.memoized_cal(nums, i, k)
            temp_ans2 = self.memoized_cal(nums, k+1, j)
            k += 1

    def maxSubArray(self, nums: List[int]) -> int:
        return self.memoized_cal(nums, 0, len(nums)-1)


obj = Solution()
nums = [5,4,-1,7,8]
print(obj.maxSubArray(nums))
