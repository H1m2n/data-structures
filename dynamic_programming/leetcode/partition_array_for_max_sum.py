from typing import List


class Solution:
    def solve(self, arr, i, j, k, dp):
        while i <= j:
            

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {}
        out = self.solve(arr, 0, len(arr) - 1, k, dp)
        print(out)
        return 0


#
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3

# arr = [1]
# k = 1
obj = Solution()
obj.maxSumAfterPartitioning(arr, k)
