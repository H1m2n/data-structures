import copy


# brute force solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_pairs = []
        nums_copy = copy.copy(nums)
        while nums_copy:
            for i, x in enumerate(nums_copy):
                pair = nums_copy[i:]
                # print(pair)
                all_pairs.append(pair)
            nums_copy.pop()
        sum_amounts = []
        for x in all_pairs:
            sum_amounts.append(sum(x))
        return max(sum_amounts)


obj = Solution()
sum_amount = obj.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])
print(sum_amount)

from sys import maxint


# optimal solution
class Solution1(object):
    """
    solved using kadane's algorithm

    Steps ->
    Initialize:
        max_so_far = INT_MIN
        max_ending_here = 0

    Loop for each element of the array
      (a) max_ending_here = max_ending_here + a[i]
      (b) if(max_so_far < max_ending_here)
                max_so_far = max_ending_here
      (c) if(max_ending_here < 0)
                max_ending_here = 0
    return max_so_far
    """

    def maxSubArray(self, nums):
        best_sum, max_ending_here = (-maxint - 1, 0)
        for x in nums:
            max_ending_here = max_ending_here + x
            if best_sum < max_ending_here:
                best_sum = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return best_sum


obj1 = Solution1()
sum_amount = obj1.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])
print(sum_amount)
