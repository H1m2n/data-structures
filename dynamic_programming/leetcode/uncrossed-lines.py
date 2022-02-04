# https://leetcode.com/problems/uncrossed-lines/
from typing import List


class Solution:
    def solve(self, nums1, nums2, i, j, dp):
        if i == 0 or j == 0:
            return 0

        if nums1[i - 1] == nums2[j - 1]:
            dp[(i, j)] = 1 + self.solve(nums1, nums2, i - 1, j - 1, dp)
        else:
            dp[(i, j)] = max(self.solve(nums1, nums2, i - 1, j, dp), self.solve(nums1, nums2, i, j - 1, dp))
        return dp[(i, j)]

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        return self.solve(nums1, nums2, len(nums1), len(nums2), dp)


obj = Solution()
nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
#
# nums1 = [2, 5, 1, 2, 5]
# nums2 = [10, 5, 2, 1, 5, 2]

# nums1 = [1, 3, 7, 1, 7, 5]
# nums2 = [1, 9, 2, 5, 1]
# nums1 = [1, 1, 2]
# nums2 = [1, 2, 1]

# nums1 = [3]
# nums2 = [3, 3, 2]

# nums1 = [2, 1]
# nums2 = [1, 2, 1, 3, 3, 2]
print(obj.maxUncrossedLines(nums1, nums2))
