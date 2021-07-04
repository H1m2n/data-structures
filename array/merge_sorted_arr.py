from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, l = (m - 1, n - 1, len(nums1) - 1)
        while l >= 0:
            if i < 0:
                nums1[l] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[l] = nums1[i]
                i -= 1
            else:
                if nums1[i] < nums2[j]:
                    nums1[l] = nums2[j]
                    j -= 1
                else:
                    nums1[l] = nums1[i]
                    i -= 1

            l -= 1
        print(nums1)
 

obj = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
obj.merge(nums1, m, nums2, n)

# [1, 2, 3, 0, 0, 10]
# [1, 2, 3, 0, 5, 10]

# [1, 1, 2, 3, 5, 10]

# [1, 2, 3, 0, 0, 0]
# [1, 2, 3]

# [1, 1, 2, 3, 2, 3]
