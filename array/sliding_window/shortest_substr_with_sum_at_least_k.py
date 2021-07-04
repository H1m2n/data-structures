from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        i, j = (0, 0)
        e_sum = 0
        min_window = 50001
        while j < len(nums):
            e_sum += nums[j]
            if e_sum < k:
                j += 1
            elif e_sum >= k:
                while e_sum >= k:
                    min_window = min(min_window, j - i + 1)
                    e_sum -= nums[i]
                    i += 1
                j += 1

        if min_window == 50001:
            return -1
        return min_window


# [2, -2, 2, -1, 1, -1, 2]

obj = Solution()
nums = [1, -2, 2, -1, 2, -10, -12]
# nums = [2, -2, 2, -1, 1, -1, 2]
k = 3
print(obj.shortestSubarray(nums, k))
