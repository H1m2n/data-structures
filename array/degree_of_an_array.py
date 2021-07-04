# from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # smallest length of subarray == degree of nums
        freq_map = {}
        # in freq map put also distance
        for i, x in enumerate(nums):
            if x not in freq_map:
                freq_map[x] = [i]
            else:
                freq_map[x].append(i)
        print(freq_map)

        degree, min_dist, num = (0, 50001, None)
        res = []
        for k, v in freq_map.items():
            freq = len(v)
            if degree <= freq:
                degree = freq
                dist = v[-1] - v[0]
                num = k
                res.append([num, dist, degree])
        # res = sorted()
        res = sorted(res, key=lambda x: (-x[-1], x[1]))
        # print(res)
        num = res[0][0]
        # in case because of 2 numbers, degree is decided, as we need to find the smallest possible length of contiguos subaaray so we need to find num that is located neary by itself

        i, j, max_freq = (0, len(nums) - 1, degree)
        c = 0
        while nums[i] != nums[j]:
            print(i, j)
            # we should break if nums[i] == nums[j], because we got the corners of a window
            if nums[i] != num and nums[j] != num:
                i += 1
                j -= 1
            elif nums[i] == num and nums[j] != num:
                j -= 1
            elif nums[i] != num and nums[j] == num:
                i += 1
        return j - i + 1


obj = Solution()
# nums = [1, 2, 2, 3, 1]
nums = [1, 2, 2, 3, 1, 4, 2]
nums = [1, 2, 2, 3, 1]
# [1,2,2,3,1,4,2]
print(obj.findShortestSubArray(nums))
