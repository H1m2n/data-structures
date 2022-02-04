from typing import List


# from collections import deque

class SolutionBk:
    def get_subarray_sum(self, out, input, limit, start, out_dict):
        if start > len(input) - 1:
            return out

        op1 = out
        if len(op1) < limit:
            # choice for picking up is available
            op1.append((start, input[start]))
            self.get_subarray_sum(op1, input, limit, start + 1, out_dict)

        op2 = out
        # choice for not including any element is only available if out is empty
        if len(out) == 0:
            self.get_subarray_sum(op2, input, limit, start + 1, out_dict)

        if len(out) == limit:
            idx_list = []
            ele_sum = 0
            for idx, ele in out:
                idx_list.append(idx)
                ele_sum += ele
            out_dict[tuple(idx_list)] = ele_sum
            out = []
            self.get_subarray_sum(out, input, limit, start + 1, out_dict)
        return out

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        start, first_out_dict, second_out_dict = (0, {}, {})
        self.get_subarray_sum([], nums, firstLen, start, first_out_dict)
        self.get_subarray_sum([], nums, secondLen, start, second_out_dict)
        print(first_out_dict)
        print(second_out_dict)


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        L array appearing first and then M array
        or
        M array appearing first and then L array
        Therefore for a given index i in the loop:
        find maximum sum for L length before index i and add it with every M length sum right to it --------(equation 1)
        find maximum sum for M length before index i and add it with every L length sum right to it---------(equation 2)
        now in every loop do res = max(res , max( equation 1, equation 2))

        This way overlapping is also avoided
        """
        # n = len(nums)
        # preSum = [0] * (n + 1)
        # i = 0
        # while i < n:
        #     preSum[i + 1] = nums[i] + preSum[i]
        #     i += 1
        # print(preSum)
        # res, lMax, mMax = (preSum[firstLen + secondLen], preSum[firstLen], preSum[secondLen])
        #
        # # print(lMax, mMax)
        # j = firstLen + secondLen
        # while j <= n:
        #     # case 1: firstLen subarray is always before secondLen
        #     print(j, preSum[j - secondLen - firstLen], preSum[j - secondLen])
        #     lMax = max(lMax, preSum[j - secondLen] - preSum[j - secondLen - firstLen])
        #     # case 2: secondLen subarray is always before firstLen subarray
        #     mMax = max(mMax, preSum[j - firstLen] - preSum[j - secondLen - firstLen])
        #     res = max(res, lMax + preSum[j] - preSum[j - secondLen], mMax + preSum[j] - preSum[j - firstLen])
        #     j += 1
        # return res

        # will store max sum of firstLen window size array till ith index from left side
        dp1 = [None] * len(nums)
        i = 0
        e_sum = 0
        while i < len(nums):
            if i < firstLen:
                e_sum += nums[i]
                dp1[i] = e_sum
            else:
                # in window we including current index element and removing i - firstLen from e_sum
                e_sum += nums[i] - nums[i - firstLen]
                dp1[i] = max(dp1[i - 1], e_sum)
            i += 1

        # will store max sum of secondLen window size array till jth index from right side
        dp2 = [None] * len(nums)
        j = len(nums) - 1
        e_sum = 0
        while j >= 0:
            if j + secondLen >= len(nums):
                e_sum += nums[j]
                dp2[j] = e_sum
            else:
                e_sum += nums[j] - nums[j + secondLen]
                dp2[j] = max(dp2[j + 1], e_sum)
            j -= 1
        ans_1_case = 0
        i = firstLen - 1
        while i < len(nums) - secondLen:
            ans_1_case = max(ans_1_case, dp1[i] + dp2[i + 1]) # will need to add dp1 and dp2, because in
            # dp1 we storing max sum from left side and in dp2 we storing max sum from left side
            i += 1

        dp1 = [None] * len(nums)
        i = 0
        e_sum = 0
        while i < len(nums):
            if i < secondLen:
                e_sum += nums[i]
                dp1[i] = e_sum
            else:
                # in window we including current index element and removing i - firstLen from e_sum
                e_sum += nums[i] - nums[i - secondLen]
                dp1[i] = max(dp1[i - 1], e_sum)
            i += 1

        # will store max sum of secondLen window size array till jth index from right side
        dp2 = [None] * len(nums)
        j = len(nums) - 1
        e_sum = 0
        while j >= 0:
            if j + firstLen >= len(nums):
                e_sum += nums[j]
                dp2[j] = e_sum
            else:
                e_sum += nums[j] - nums[j + firstLen]
                dp2[j] = max(dp2[j + 1], e_sum)
            j -= 1
        ans_2_case = 0
        i = secondLen - 1
        while i < len(nums) - firstLen:
            ans_2_case = max(ans_2_case, dp1[i] + dp2[i + 1])
            i += 1
        return max(ans_1_case, ans_2_case)


obj = Solution()
# nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
# firstLen = 1
# secondLen = 2
nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
firstLen = 3
secondLen = 2
print(obj.maxSumTwoNoOverlap(nums, firstLen, secondLen))
