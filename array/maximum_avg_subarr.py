from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 10
        # 7
        # [5, 4, 1, 2, 10, 3, 6, 8, 9]
        i, j = (0, 0)
        e_sum = 0
        max_sum = None
        while j < len(nums):
            e_sum += nums[j]
            window_size = j - i + 1
            if window_size < k:
                j += 1
            elif window_size == k:
                if max_sum is None:
                    max_sum = e_sum
                else:
                    max_sum = max(max_sum, e_sum)
                e_sum -= nums[i]
                i += 1
                j += 1
        print(max_sum)
        return max_sum / k

obj = Solution()
nums = [8860, -853, 6534, 4477, -4589, 8646, -6155, -5577, -1656, -5779, -2619, -8604, -1358, -8009, 4983, 7063, 3104, -1560,
 4080, 2763, 5616, -2375, 2848, 1394, -7173, -5225, -8244, -809, 8025, -4072, -4391, -9579, 1407, 6700, 2421, -6685,
 5481, -1732, -8892, -6645, 3077, 3287, -4149, 8701, -4393, -9070, -1777, 2237, -3253, -506, -4931, -7366, -8132, 5406,
 -6300, -275, -1908, 67, 3569, 1433, -7262, -437, 8303, 4498, -379, 3054, -6285, 4203, 6908, 4433, 3077, 2288, 9733,
 -8067, 3007, 9725, 9669, 1362, -2561, -4225, 5442, -9006, -429, 160, -9234, -4444, 3586, -5711, -9506, -79, -4418,
 -4348, -5891]
k = 93

print(obj.findMaxAverage(nums, k))
